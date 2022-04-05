from bancorml.environments.tokenomics.tokenomics_base import TokenomicsBase


class FixedPointTokenomics(TokenomicsBase):
    """Tokenomics subclass for all fixed-point arithmetic.
    """

    MAX_UINT256 = 2 ** 256 - 1
    MAX_UINT128 = 2 ** 128 - 1

    """Tokenomics subclass for all floating-point arithmetic.
        """

    def check_surplus(self, b, c, e, n, is_surplus=False, is_deficit=True, case='check surplus'):
        self.validate_signage_and_overflow(b + c)
        self.validate_signage_and_overflow(1 - n)
        if (b + c) // (1 - n) > e: is_surplus, is_deficit = True, False
        self.surplus, self.deficit = is_surplus, is_deficit

    def check_hlim(self, b, c, e, x):
        self.validate_signage_and_overflow(c * e)
        self.validate_signage_and_overflow(b + c)
        hlim = (c * e) // (b + c)
        satisfies_hlim = hlim > x
        self.hlim, self.satisfies_hlim = hlim, satisfies_hlim

    def check_hmax(self, b, c, e, m, n, x, is_surplus):
        if is_surplus:
            self.validate_signage_and_overflow(b * e * (e * n + m * (b + c - e)))
            self.validate_signage_and_overflow((1 - m) * (b + c - e) * (b + c - e * (1 - n)))
        else:
            self.validate_signage_and_overflow(b * e * (e * n - m * (b + c - e * (1 - n))))
            self.validate_signage_and_overflow((1 - m) * (b + c - e) * (b + c - e * (1 - n)))
        hmax = b * e * (e * n + m * (b + c - e)) // (
                (1 - m) * (b + c - e) * (b + c - e * (1 - n))) if is_surplus else b * e * (
                e * n - m * (b + c - e * (1 - n))) // ((1 - m) * (b + c - e) * (b + c - e * (1 - n)))
        satisfies_hmax = hmax > x
        self.hmax, self.satisfies_hmax = hmax, satisfies_hmax

    def check_reduce_trading_liquidity(self, x, b, c, e, n, is_surplus, satisfies_hmax, satisfies_hlim,
                                       case='check reduce_trading_liquidity', reduce_trading_liquidity=False):
        if (satisfies_hmax == False) or (satisfies_hlim == False):
            reduce_trading_liquidity = (x * (1 - n)) <= c if is_surplus else ((x * (1 - n) * (b + c)) // e) <= c
        self.reduce_trading_liquidity = reduce_trading_liquidity

    def handle_bootstrap_surplus(self, x, n):
        self.validate_signage_and_overflow(1 - n)
        self.validate_signage_and_overflow(x * (1 - n))
        s = x * (1 - n)
        return s

    def handle_bootstrap_deficit_special_case(self, c, e, n, x):
        self.validate_signage_and_overflow(1 - n)
        self.validate_signage_and_overflow(c * x)
        self.validate_signage_and_overflow(c * x * (1 - n))
        s = c * x * (1 - n) // e
        return s

    def handle_arbitrage_surplus(self, x, n, a, b, c, e, m):
        self.validate_signage_and_overflow(1 - n)
        self.validate_signage_and_overflow(x * (1 - n))
        self.validate_signage_and_overflow(a * x * (b + c - e * (1 - n)))
        self.validate_signage_and_overflow((1 - m) * (b * e + x * (b + c - e * (1 - n))))
        self.validate_signage_and_overflow(x * (b + c - e * (1 - n)))
        s = x * (1 - n)
        p = a * x * (b + c - e * (1 - n)) // ((1 - m) * (b * e + x * (b + c - e * (1 - n))))
        r = x * (b + c - e * (1 - n)) // e
        return p, r, s

    def handle_default_surplus(self, x, n, c, a, b):
        self.validate_signage_and_overflow(x * (1 - n) - c)
        self.validate_signage_and_overflow(x * (1 - n))
        self.validate_signage_and_overflow(a * (x * (1 - n) - c))
        r = x * (1 - n) - c
        s = x * (1 - n)
        p = q = a * (x * (1 - n) - c) // b
        return p, q, r, s


    def handle_arbitrage_deficit(self, x, n, a, m, e, b, c):
        self.validate_signage_and_overflow(a * x * (1 - m) * (e * (1 - n) - b - c))
        self.validate_signage_and_overflow(x * (1 - n))
        self.validate_signage_and_overflow(x * (e * (1 - n) - b - c))
        s = x * (1 - n)
        p = a * x * (1 - m) * (e * (1 - n) - b - c) // (b * e - x * (1 - m) * (e * (1 - n) - b - c))
        r = x * (e * (1 - n) - b - c) // e
        return p, r, s

    def handle_bootstrap_deficit(self, x, n, b, c, e, a):
        self.validate_signage_and_overflow(x * (1 - n) * (b + c))
        self.validate_signage_and_overflow(a * x * (1 - n) * (e - b - c))
        s = x * (1 - n) * (b + c) // e
        t = a * x * (1 - n) * (e - b - c) // (b * e)
        return s, t

    def handle_default_deficit(self, a, b, c, e, n, x):
        self.validate_signage_and_overflow(x * (1 - n) * (b + c))
        self.validate_signage_and_overflow(x * (1 - n) * (b + c) - c * e)
        p = q = (a * (b * e - (b + c) * (e - x * (1 - n)))) // (b * e)
        r = (x * (1 - n) * (b + c) - c * e) // e
        s = (x * (1 - n) * (b + c)) // e
        t = (a * x * (1 - n) * (e - b - c)) // (b * e)
        return p, q, r, s, t

    def handle_external_wallet_adjustment_1(self, t, b, a):
        self.validate_signage_and_overflow(t * b)
        u = (t * b) // a
        t = 0
        return t, u

    def handle_external_wallet_adjustment_2(self, w, t, b, a):
        self.validate_signage_and_overflow(t * b - a * w)
        u = w
        t = (t * b - a * w) // b
        return t, u

    def handle_trade_bnt_to_tkn(self, a, d, b, x, e):
        self.validate_signage_and_overflow(a * (a + x) + d * (1 - e) * (a * x + x * x))
        self.validate_signage_and_overflow(b * (a + d * x))
        bnt_trading_liquidity = (a * (a + x) + d * (1 - e) * (a * x + x * x)) // (a + d * x)
        tkn_trading_liquidity = (b * (a + d * x)) // (a + x)
        tkn_out = (b * x * (1 - d)) // (a + x)
        tkn_fee = (b * d * x * (1 - e)) // (a + x)
        vortex_fee = (d * e * x * (a + x)) // (a + d * x)
        return bnt_trading_liquidity, tkn_trading_liquidity, tkn_out, tkn_fee, vortex_fee

    def handle_trade_tkn_to_bnt(self, a, d, b, x, e):
        self.validate_signage_and_overflow(a * (b + d * x * (1 - e)))
        self.validate_signage_and_overflow(b + x)
        bnt_trading_liquidity = (a * (b + d * x * (1 - e))) // (b + x)
        tkn_trading_liquidity = b + x
        bnt_out = (a * x * (1 - d)) // (b + x)
        bnt_fee = (a * d * x * (1 - e)) // (b + x)
        vortex_fee = (a * d * e * x) // (b + x)
        return bnt_trading_liquidity, tkn_trading_liquidity, bnt_out, bnt_fee, vortex_fee

    def handle_trade_tkn_to_tkn(self, a1, d1, b1, a2, d2, b2, x, e):
        self.validate_signage_and_overflow(a1 * (b1 + d1 * x * (1 - e)))
        self.validate_signage_and_overflow(b1 + x)
        bnt_source_trading_liquidity = (a1 * (b1 + d1 * x * (1 - e))) // (b1 + x)
        tkn_source_trading_liquidity = b1 + x
        bnt_destination_trading_liquidity = ((a1 * x * (1 - d1) + a2 * (b1 + x)) * (
                    a1 * d2 * x * (1 - d1) * (1 - e) + a2 * (b1 + x))) // (
                                                        (b1 + x) * (a1 * d2 * x * (1 - d1) + a2 * (b1 + x)))
        tkn_destination_trading_liquidity = (b2 * (a1 * d2 * x * (1 - d1) + a2 * (b1 + x))) // (
                    a1 * x * (1 - d1) + a2 * (b1 + x))
        tkn_out = (a1 * b2 * x * (1 - d1) * (1 - d2)) // (a1 * x * (1 - d1) + a2 * (b1 + x))
        bnt_fee = (a1 * d1 * x * (1 - e)) // (b1 + x)
        tkn_fee = (a1 * b2 * d2 * x * (1 - d1) * (1 - e)) // (a1 * x * (1 - d1) + a2 * (b1 + x))
        vortex_fee = (a1 * e * x * (a1 * d2 * x * (1 - d1) + a2 * (b1 + x) * (d1 + d2 - d1 * d2))) // (
                    (b1 + x) * (a1 * d2 * x * (1 - d1) + a2 * (b1 + x)))
        return bnt_source_trading_liquidity, tkn_source_trading_liquidity, bnt_destination_trading_liquidity, tkn_destination_trading_liquidity, tkn_out, bnt_fee, tkn_fee, vortex_fee

    def validate_signage_and_overflow(self, val):
        assert 0 <= val, 'signage::{}'.format(val)
        assert val <= FixedPointTokenomics.MAX_UINT256, 'overflow::{}'.format(val)
