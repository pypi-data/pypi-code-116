"""Generated wrapper for DepositContract Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    Any,
    List,
    Optional,
    Tuple,
    Union,
)
import time
from eth_utils import to_checksum_address
from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3 import Web3
from web3.contract import ContractFunction
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider
from web3.exceptions import ContractLogicError
from moody.m.bases import ContractMethod, Validator, ContractBase, Signatures
from moody.m.tx_params import TxParams
from moody.libeb import MiliDoS
from moody import Bolors

# Try to import a custom validator class definition; if there isn't one,
# declare one that we can instantiate for the default argument to the
# constructor for DepositContract below.
try:
    # both mypy and pylint complain about what we're doing here, but this
    # works just fine, so their messages have been disabled here.
    from . import (  # type: ignore # pylint: disable=import-self
        DepositContractValidator,
    )
except ImportError:

    class DepositContractValidator(  # type: ignore
        Validator
    ):
        """No-op input validator."""

try:
    from .middleware import MIDDLEWARE  # type: ignore
except ImportError:
    pass


class DepositMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the deposit method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("deposit")

    def validate_and_normalize_inputs(self, pubkey: Union[bytes, str], withdrawal_credentials: Union[bytes, str], signature: Union[bytes, str], deposit_data_root: Union[bytes, str]) -> any:
        """Validate the inputs to the deposit method."""
        self.validator.assert_valid(
            method_name='deposit',
            parameter_name='pubkey',
            argument_value=pubkey,
        )
        self.validator.assert_valid(
            method_name='deposit',
            parameter_name='withdrawal_credentials',
            argument_value=withdrawal_credentials,
        )
        self.validator.assert_valid(
            method_name='deposit',
            parameter_name='signature',
            argument_value=signature,
        )
        self.validator.assert_valid(
            method_name='deposit',
            parameter_name='deposit_data_root',
            argument_value=deposit_data_root,
        )
        return (pubkey, withdrawal_credentials, signature, deposit_data_root)

    def block_send(self, pubkey: Union[bytes, str], withdrawal_credentials: Union[bytes, str], signature: Union[bytes, str], deposit_data_root: Union[bytes, str], _valeth: int = 0) -> None:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(pubkey, withdrawal_credentials, signature, deposit_data_root)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("deposit", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: deposit")
            message = f"Error {er}: deposit"
            self._on_fail("deposit", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, deposit: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, deposit. Reason: Unknown")

            self._on_fail("deposit", message)

    def send_transaction(self, pubkey: Union[bytes, str], withdrawal_credentials: Union[bytes, str], signature: Union[bytes, str], deposit_data_root: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (pubkey, withdrawal_credentials, signature, deposit_data_root) = self.validate_and_normalize_inputs(pubkey, withdrawal_credentials, signature, deposit_data_root)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pubkey, withdrawal_credentials, signature, deposit_data_root).transact(tx_params.as_dict())

    def build_transaction(self, pubkey: Union[bytes, str], withdrawal_credentials: Union[bytes, str], signature: Union[bytes, str], deposit_data_root: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (pubkey, withdrawal_credentials, signature, deposit_data_root) = self.validate_and_normalize_inputs(pubkey, withdrawal_credentials, signature, deposit_data_root)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pubkey, withdrawal_credentials, signature, deposit_data_root).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, pubkey: Union[bytes, str], withdrawal_credentials: Union[bytes, str], signature: Union[bytes, str], deposit_data_root: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (pubkey, withdrawal_credentials, signature, deposit_data_root) = self.validate_and_normalize_inputs(pubkey, withdrawal_credentials, signature, deposit_data_root)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(pubkey, withdrawal_credentials, signature, deposit_data_root).estimateGas(tx_params.as_dict())


class GetDepositCountMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the get_deposit_count method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("get_deposit_count")

    def block_call(self, debug: bool = False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
            'from': self._operate
        })
        return Union[bytes, str](returned)

    def block_send(self, _valeth: int = 0) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("get_deposit_count", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_deposit_count")
            message = f"Error {er}: get_deposit_count"
            self._on_fail("get_deposit_count", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_deposit_count: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_deposit_count. Reason: Unknown")

            self._on_fail("get_deposit_count", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class GetDepositRootMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the get_deposit_root method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(elib, contract_address)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("get_deposit_root")

    def block_call(self, debug: bool = False) -> Union[bytes, str]:
        _fn = self._underlying_method()
        returned = _fn.call({
            'from': self._operate
        })
        return Union[bytes, str](returned)

    def block_send(self, _valeth: int = 0) -> Union[bytes, str]:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method()
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("get_deposit_root", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: get_deposit_root")
            message = f"Error {er}: get_deposit_root"
            self._on_fail("get_deposit_root", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_deposit_root: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, get_deposit_root. Reason: Unknown")

            self._on_fail("get_deposit_root", message)

    def send_transaction(self, tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().transact(tx_params.as_dict())

    def build_transaction(self, tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().buildTransaction(tx_params.as_dict())

    def estimate_gas(self, tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method().estimateGas(tx_params.as_dict())


class SupportsInterfaceMethod(ContractMethod):  # pylint: disable=invalid-name
    """Various interfaces to the supportsInterface method."""

    def __init__(self, elib: MiliDoS, contract_address: str, contract_function: ContractFunction, validator: Validator = None):
        """Persist instance data."""
        super().__init__(elib, contract_address, validator)
        self._underlying_method = contract_function
        self.sign = validator.getSignature("supportsInterface")

    def validate_and_normalize_inputs(self, interface_id: Union[bytes, str]) -> any:
        """Validate the inputs to the supportsInterface method."""
        self.validator.assert_valid(
            method_name='supportsInterface',
            parameter_name='interfaceId',
            argument_value=interface_id,
        )
        return (interface_id)

    def block_call(self, interface_id: Union[bytes, str], debug: bool = False) -> bool:
        _fn = self._underlying_method(interface_id)
        returned = _fn.call({
            'from': self._operate
        })
        return bool(returned)

    def block_send(self, interface_id: Union[bytes, str], _valeth: int = 0) -> bool:
        """Execute underlying contract method via eth_call.

        :param tx_params: transaction parameters
        :returns: the return value of the underlying method.
        """
        _fn = self._underlying_method(interface_id)
        try:

            _t = _fn.buildTransaction({
                'from': self._operate,
                'gas': self.gas_limit,
                'gasPrice': self.gas_price_wei
            })
            _t['nonce'] = self._web3_eth.getTransactionCount(self._operate)

            if _valeth > 0:
                _t['value'] = _valeth

            if self.debug_method:
                print(f"======== Signing ✅ by {self._operate}")
                print(f"======== Transaction ✅ check")
                print(_t)

            if 'data' in _t:

                signed = self._web3_eth.account.sign_transaction(_t)
                txHash = self._web3_eth.sendRawTransaction(signed.rawTransaction)
                tx_receipt = None
                if self.auto_reciept is True:
                    print(f"======== awaiting Confirmation 🚸️ {self.sign}")
                    tx_receipt = self._web3_eth.wait_for_transaction_receipt(txHash)
                    if self.debug_method:
                        print("======== TX Result ✅")
                        print(tx_receipt)

                self._on_receipt_handle("supports_interface", tx_receipt, txHash)

            if self.auto_reciept is False:
                time.sleep(self._wait)


        except ContractLogicError as er:
            print(f"{Bolors.FAIL}Error {er} {Bolors.RESET}: supports_interface")
            message = f"Error {er}: supports_interface"
            self._on_fail("supports_interface", message)
        except ValueError as err:
            if "message" in err.args[0]:
                message = err.args[0]["message"]
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, supports_interface: {message}")
            else:
                message = "Error Revert , Reason: Unknown"
                print(f"{Bolors.FAIL}Error Revert {Bolors.RESET}, supports_interface. Reason: Unknown")

            self._on_fail("supports_interface", message)

    def send_transaction(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> Union[HexBytes, bytes]:
        """Execute underlying contract method via eth_sendTransaction.

        :param tx_params: transaction parameters
        """
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).transact(tx_params.as_dict())

    def build_transaction(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> dict:
        """Construct calldata to be used as input to the method."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).buildTransaction(tx_params.as_dict())

    def estimate_gas(self, interface_id: Union[bytes, str], tx_params: Optional[TxParams] = None) -> int:
        """Estimate gas consumption of method call."""
        (interface_id) = self.validate_and_normalize_inputs(interface_id)
        tx_params = super().normalize_tx_params(tx_params)
        return self._underlying_method(interface_id).estimateGas(tx_params.as_dict())


class SignatureGenerator(Signatures):
    """
        The signature is generated for this and it is installed.
    """

    def __init__(self, abi: any):
        super().__init__(abi)

    def deposit(self) -> str:
        return self._function_signatures["deposit"]

    def get_deposit_count(self) -> str:
        return self._function_signatures["get_deposit_count"]

    def get_deposit_root(self) -> str:
        return self._function_signatures["get_deposit_root"]

    def supports_interface(self) -> str:
        return self._function_signatures["supportsInterface"]


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class DepositContract(ContractBase):
    """Wrapper class for DepositContract Solidity contract.

    All method parameters of type `bytes`:code: should be encoded as UTF-8,
    which can be accomplished via `str.encode("utf_8")`:code:.
    """
    _fn_deposit: DepositMethod
    """Constructor-initialized instance of
    :class:`DepositMethod`.
    """

    _fn_get_deposit_count: GetDepositCountMethod
    """Constructor-initialized instance of
    :class:`GetDepositCountMethod`.
    """

    _fn_get_deposit_root: GetDepositRootMethod
    """Constructor-initialized instance of
    :class:`GetDepositRootMethod`.
    """

    _fn_supports_interface: SupportsInterfaceMethod
    """Constructor-initialized instance of
    :class:`SupportsInterfaceMethod`.
    """

    SIGNATURES: SignatureGenerator = None

    def __init__(
            self,
            core_lib: MiliDoS,
            contract_address: str,
            validator: DepositContractValidator = None,
    ):
        """Get an instance of wrapper for smart contract.
        """
        # pylint: disable=too-many-statements
        super().__init__(contract_address, DepositContract.abi())
        web3 = core_lib.w3

        if not validator:
            validator = DepositContractValidator(web3, contract_address)

        # if any middleware was imported, inject it
        try:
            MIDDLEWARE
        except NameError:
            pass
        else:
            try:
                for middleware in MIDDLEWARE:
                    web3.middleware_onion.inject(
                        middleware['function'], layer=middleware['layer'],
                    )
            except ValueError as value_error:
                if value_error.args == ("You can't add the same un-named instance twice",):
                    pass

        self._web3_eth = web3.eth
        functions = self._web3_eth.contract(address=to_checksum_address(contract_address), abi=DepositContract.abi()).functions
        self._signatures = SignatureGenerator(DepositContract.abi())
        validator.bindSignatures(self._signatures)

        self._fn_deposit = DepositMethod(core_lib, contract_address, functions.deposit, validator)
        self._fn_get_deposit_count = GetDepositCountMethod(core_lib, contract_address, functions.get_deposit_count, validator)
        self._fn_get_deposit_root = GetDepositRootMethod(core_lib, contract_address, functions.get_deposit_root, validator)
        self._fn_supports_interface = SupportsInterfaceMethod(core_lib, contract_address, functions.supportsInterface, validator)

    def event_deposit_event(
            self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """
        Implementation of event deposit_event in contract DepositContract
        Get log entry for DepositEvent event.
                :param tx_hash: hash of transaction emitting DepositEvent event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return self._web3_eth.contract(address=to_checksum_address(self.contract_address), abi=DepositContract.abi()).events.DepositEvent().processReceipt(tx_receipt)

    def deposit(self, pubkey: Union[bytes, str], withdrawal_credentials: Union[bytes, str], signature: Union[bytes, str], deposit_data_root: Union[bytes, str], wei: int = 0) -> None:
        """
        Implementation of deposit in contract DepositContract
        Method of the function
    
        """

        self._fn_deposit.callback_onfail = self._callback_onfail
        self._fn_deposit.callback_onsuccess = self._callback_onsuccess
        self._fn_deposit.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_deposit.gas_limit = self.call_contract_fee_amount
        self._fn_deposit.gas_price_wei = self.call_contract_fee_price
        self._fn_deposit.debug_method = self.call_contract_debug_flag

        self._fn_deposit.wei_value = wei

        return self._fn_deposit.block_send(pubkey, withdrawal_credentials, signature, deposit_data_root, wei)

    def get_deposit_count(self) -> Union[bytes, str]:
        """
        Implementation of get_deposit_count in contract DepositContract
        Method of the function
    
        """

        self._fn_get_deposit_count.callback_onfail = self._callback_onfail
        self._fn_get_deposit_count.callback_onsuccess = self._callback_onsuccess
        self._fn_get_deposit_count.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_deposit_count.gas_limit = self.call_contract_fee_amount
        self._fn_get_deposit_count.gas_price_wei = self.call_contract_fee_price
        self._fn_get_deposit_count.debug_method = self.call_contract_debug_flag

        return self._fn_get_deposit_count.block_call()

    def get_deposit_root(self) -> Union[bytes, str]:
        """
        Implementation of get_deposit_root in contract DepositContract
        Method of the function
    
        """

        self._fn_get_deposit_root.callback_onfail = self._callback_onfail
        self._fn_get_deposit_root.callback_onsuccess = self._callback_onsuccess
        self._fn_get_deposit_root.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_get_deposit_root.gas_limit = self.call_contract_fee_amount
        self._fn_get_deposit_root.gas_price_wei = self.call_contract_fee_price
        self._fn_get_deposit_root.debug_method = self.call_contract_debug_flag

        return self._fn_get_deposit_root.block_call()

    def supports_interface(self, interface_id: Union[bytes, str]) -> bool:
        """
        Implementation of supports_interface in contract DepositContract
        Method of the function
    
        """

        self._fn_supports_interface.callback_onfail = self._callback_onfail
        self._fn_supports_interface.callback_onsuccess = self._callback_onsuccess
        self._fn_supports_interface.auto_reciept = self.call_contract_enforce_tx_receipt
        self._fn_supports_interface.gas_limit = self.call_contract_fee_amount
        self._fn_supports_interface.gas_price_wei = self.call_contract_fee_price
        self._fn_supports_interface.debug_method = self.call_contract_debug_flag

        return self._fn_supports_interface.block_call(interface_id)

    def CallContractWait(self, t_long: int) -> "DepositContract":
        self._fn_deposit.setWait(t_long)
        self._fn_get_deposit_count.setWait(t_long)
        self._fn_get_deposit_root.setWait(t_long)
        self._fn_supports_interface.setWait(t_long)
        return self

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bytes","name":"pubkey","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"withdrawal_credentials","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"amount","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"signature","type":"bytes"},{"indexed":false,"internalType":"bytes","name":"index","type":"bytes"}],"name":"DepositEvent","type":"event"},{"inputs":[{"internalType":"bytes","name":"pubkey","type":"bytes"},{"internalType":"bytes","name":"withdrawal_credentials","type":"bytes"},{"internalType":"bytes","name":"signature","type":"bytes"},{"internalType":"bytes32","name":"deposit_data_root","type":"bytes32"}],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"get_deposit_count","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"get_deposit_root","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"pure","type":"function"}]'
            # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
