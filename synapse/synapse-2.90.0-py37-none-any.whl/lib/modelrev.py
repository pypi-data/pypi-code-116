import logging

import synapse.exc as s_exc
import synapse.common as s_common

import synapse.lib.layer as s_layer

logger = logging.getLogger(__name__)

maxvers = (0, 2, 8)

class ModelRev:

    def __init__(self, core):
        self.core = core
        self.revs = (
            ((0, 2, 1), self.revModel20210126),
            ((0, 2, 2), self.revModel20210312),
            ((0, 2, 3), self.revModel20210528),
            ((0, 2, 5), self.revModel20210801),
            ((0, 2, 6), self.revModel20211112),
            ((0, 2, 7), self.revModel20220307),
            ((0, 2, 8), self.revModel20220315),
        )

    async def _uniqSortArray(self, todoprops, layers):

        for layr in layers:

            for propname in todoprops:

                nodeedits = []
                meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

                def sortuniq(valu):
                    return tuple(sorted({v: True for v in valu}.keys()))

                async def save():
                    await layr.storNodeEdits(nodeedits, meta)
                    nodeedits.clear()

                prop = self.core.model.prop(propname)
                if prop is None:
                    logger.warning(f'No property named {propname} to sortuniq().')
                    continue

                propreln = prop.name
                formname = prop.form.name

                stortype = prop.type.stortype | s_layer.STOR_FLAG_ARRAY

                async for buid, propvalu in layr.iterPropRows(formname, propreln):

                    uniqvalu = sortuniq(propvalu)
                    if uniqvalu == propvalu:
                        continue

                    nodeedits.append(
                        (buid, formname, (
                            (s_layer.EDIT_PROP_SET, (propreln, uniqvalu, propvalu, stortype), ()),
                        )),
                    )

                    if len(nodeedits) >= 1000:
                        await save()

                if nodeedits:
                    await save()

    async def revModel20211112(self, layers):
        # uniq and sort several array types
        todoprops = (
            'biz:rfp:requirements',

            'crypto:x509:cert:ext:sans',
            'crypto:x509:cert:ext:crls',
            'crypto:x509:cert:identities:fqdns',
            'crypto:x509:cert:identities:emails',
            'crypto:x509:cert:identities:ipv4s',
            'crypto:x509:cert:identities:ipv6s',
            'crypto:x509:cert:identities:urls',
            'crypto:x509:cert:crl:urls',

            'inet:whois:iprec:contacts',
            'inet:whois:iprec:links',
            'inet:whois:ipcontact:roles',
            'inet:whois:ipcontact:links',
            'inet:whois:ipcontact:contacts',

            'it:account:groups',
            'it:group:groups',

            'it:reveng:function:impcalls',
            'it:reveng:filefunc:funccalls',

            'it:sec:cve:references',

            'risk:vuln:cwes',

            'tel:txtmesg:recipients',
        )
        await self._uniqSortArray(todoprops, layers)

    async def revModel20210801(self, layers):

        # uniq and sort several array types
        todoprops = (
            'edu:course:prereqs',
            'edu:class:assistants',

            'ou:org:subs',
            'ou:org:names',
            'ou:org:dns:mx',
            'ou:org:locations',
            'ou:org:industries',

            'ou:industry:sic',
            'ou:industry:subs',
            'ou:industry:isic',
            'ou:industry:naics',

            'ou:preso:sponsors',
            'ou:preso:presenters',

            'ou:conference:sponsors',
            'ou:conference:event:sponsors',
            'ou:conference:attendee:roles',
            'ou:conference:event:attendee:roles',

            'ou:contract:types',
            'ou:contract:parties',
            'ou:contract:requirements',
            'ou:position:reports',

            'ps:person:names',
            'ps:person:nicks',
            'ps:persona:names',
            'ps:persona:nicks',
            'ps:education:classes',
            'ps:contactlist:contacts',
        )
        await self._uniqSortArray(todoprops, layers)

    async def revModel20210528(self, layers):

        cmdtype = self.core.model.type('it:cmd')
        cmdprop = self.core.model.prop('it:exec:proc:cmd')

        for layr in layers:

            done = set()
            nodeedits = []

            meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

            async def save():
                await layr.storNodeEdits(nodeedits, meta)
                done.clear()
                nodeedits.clear()

            async for buid, propvalu in layr.iterPropRows('it:exec:proc', 'cmd'):

                cmdnorm = cmdtype.norm(propvalu)[0]

                if cmdnorm != propvalu:
                    nodeedits.append(
                        (buid, 'it:exec:proc', (
                            (s_layer.EDIT_PROP_SET, ('cmd', cmdnorm, propvalu, s_layer.STOR_TYPE_UTF8), ()),
                        )),
                    )

                if cmdnorm not in done:
                    cmdbuid = s_common.buid(('it:cmd', cmdnorm))
                    nodeedits.append(
                        (cmdbuid, 'it:cmd', (
                            (s_layer.EDIT_NODE_ADD, (cmdnorm, s_layer.STOR_TYPE_UTF8), ()),
                        )),
                    )
                    done.add(cmdnorm)

                if len(nodeedits) >= 1000:
                    await save()

            if nodeedits:
                await save()

    async def revModel20210312(self, layers):

        ipv4type = self.core.model.type('inet:ipv4')
        ipv6type = self.core.model.type('inet:ipv6')

        for layr in layers:

            nodeedits = []
            meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

            async def save():
                await layr.storNodeEdits(nodeedits, meta)
                nodeedits.clear()

            async for buid, propvalu in layr.iterPropRows('inet:web:acct', 'signup:client:ipv6'):

                ipv6text = ipv6type.norm(ipv4type.repr(propvalu))[0]
                nodeedits.append(
                    (buid, 'inet:web:acct', (
                        (s_layer.EDIT_PROP_SET, ('signup:client:ipv6', ipv6text, propvalu, s_layer.STOR_TYPE_IPV6), ()),
                    )),
                )

                if len(nodeedits) >= 1000:
                    await save()

            if nodeedits:
                await save()

    async def revModel20210126(self, layers):

        for layr in layers:

            nodeedits = []
            meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

            # uniq values of some array types....
            def uniq(valu):
                return tuple({v: True for v in valu}.keys())

            async def save():
                await layr.storNodeEdits(nodeedits, meta)
                nodeedits.clear()

            stortype = s_layer.STOR_TYPE_GUID | s_layer.STOR_FLAG_ARRAY
            async for buid, propvalu in layr.iterPropRows('ou:org', 'industries'):

                uniqvalu = uniq(propvalu)
                if uniqvalu == propvalu:
                    continue

                nodeedits.append(
                    (buid, 'ou:org', (
                        (s_layer.EDIT_PROP_SET, ('industries', uniqvalu, propvalu, stortype), ()),
                    )),
                )

                if len(nodeedits) >= 1000:
                    await save()

            if nodeedits:
                await save()

    async def _normHugeProp(self, layers, prop):

        proptype = prop.type
        propname = prop.name
        formname = prop.form.name
        stortype = prop.type.stortype

        for layr in layers:

            nodeedits = []
            meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

            async def save():
                await layr.storNodeEdits(nodeedits, meta)
                nodeedits.clear()

            async for buid, propvalu in layr.iterPropRows(formname, propname):

                try:
                    newval = proptype.norm(propvalu)[0]
                except s_exc.BadTypeValu as e:
                    oldm = e.errinfo.get('mesg')
                    logger.warning(f'Bad prop value {propname}={propvalu!r} : {oldm}')
                    continue

                if newval == propvalu:
                    continue

                nodeedits.append(
                    (buid, formname, (
                        (s_layer.EDIT_PROP_SET, (propname, newval, None, stortype), ()),
                    )),
                )

                if len(nodeedits) >= 1000:
                    await save()

            if nodeedits:
                await save()

    async def _normHugeTagProps(self, layr, tagprops):

        nodeedits = []
        meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

        async def save():
            await layr.storNodeEdits(nodeedits, meta)
            nodeedits.clear()

        for form, tag, prop in layr.getTagProps():
            if form is None or prop not in tagprops:
                continue

            tptyp = self.core.model.tagprops[prop]
            stortype = tptyp.type.stortype

            async for buid, propvalu in layr.iterTagPropRows(tag, prop, form):

                try:
                    newval = tptyp.type.norm(propvalu)[0]
                except s_exc.BadTypeValu as e:
                    oldm = e.errinfo.get('mesg')
                    logger.warning(f'Bad prop value {tag}:{prop}={propvalu!r} : {oldm}')
                    continue

                if newval == propvalu:
                    continue

                nodeedits.append(
                    (buid, form, (
                        (s_layer.EDIT_TAGPROP_SET, (tag, prop, newval, None, stortype), ()),
                    )),
                )

                if len(nodeedits) >= 1000:
                    await save()

            if nodeedits:
                await save()

    async def revModel20220307(self, layers):

        for name, prop in self.core.model.props.items():
            if prop.form is None:
                continue

            stortype = prop.type.stortype
            if stortype & s_layer.STOR_FLAG_ARRAY:
                stortype = stortype & 0x7fff

            if stortype == s_layer.STOR_TYPE_HUGENUM:
                await self._normHugeProp(layers, prop)

        tagprops = set()
        for name, prop in self.core.model.tagprops.items():
            if prop.type.stortype == s_layer.STOR_TYPE_HUGENUM:
                tagprops.add(prop.name)

        for layr in layers:
            await self._normHugeTagProps(layr, tagprops)

    async def revModel20220315(self, layers):

        meta = {'time': s_common.now(), 'user': self.core.auth.rootuser.iden}

        nodeedits = []
        for layr in layers:

            async def save():
                await layr.storNodeEdits(nodeedits, meta)
                nodeedits.clear()

            for formname, propname in (
                    ('geo:place', 'name'),
                    ('crypto:currency:block', 'hash'),
                    ('crypto:currency:transaction', 'hash')):

                prop = self.core.model.prop(f'{formname}:{propname}')
                async for buid, propvalu in layr.iterPropRows(formname, propname):
                    try:
                        norm = prop.type.norm(propvalu)[0]
                    except s_exc.BadTypeValu as e: # pragma: no cover
                        oldm = e.errinfo.get('mesg')
                        logger.warning(f'error re-norming {formname}:{propname}={propvalu} : {oldm}')
                        continue

                    if norm == propvalu:
                        continue

                    nodeedits.append(
                        (buid, formname, (
                            (s_layer.EDIT_PROP_SET, (propname, norm, propvalu, prop.type.stortype), ()),
                        )),
                    )

                    if len(nodeedits) >= 1000:  # pragma: no cover
                        await save()

                if nodeedits:
                    await save()

        layridens = [layr.iden for layr in layers]

        storm_geoplace_to_geoname = '''
        $layers = $lib.set()
        $layers.adds($layridens)
        for $view in $lib.view.list(deporder=$lib.true) {
            if (not $layers.has($view.layers.0.iden)) { continue }
            view.exec $view.iden {
                yield $lib.layer.get().liftByProp(geo:place:name)
                [ geo:name=:name ]
            }
        }
        '''

        storm_crypto_txin = '''
        $layers = $lib.set()
        $layers.adds($layridens)
        for $view in $lib.view.list(deporder=$lib.true) {
            if (not $layers.has($view.layers.0.iden)) { continue }
            view.exec $view.iden {

                function addInputXacts() {
                    yield $lib.layer.get().liftByProp(crypto:payment:input)
                    -:transaction $xact = $lib.null
                    { -> crypto:currency:transaction $xact=$node.value() }
                    if $xact {
                        [ :transaction=$xact ]
                    }
                    fini { return() }
                }

                function addOutputXacts() {
                    yield $lib.layer.get().liftByProp(crypto:payment:output)
                    -:transaction $xact = $lib.null
                    { -> crypto:currency:transaction $xact=$node.value() }
                    if $xact {
                        [ :transaction=$xact ]
                    }
                    fini { return() }
                }

                function wipeInputsArray() {
                    yield $lib.layer.get().liftByProp(crypto:currency:transaction:inputs)
                    [ -:inputs ]
                    fini { return() }
                }

                function wipeOutputsArray() {
                    yield $lib.layer.get().liftByProp(crypto:currency:transaction:outputs)
                    [ -:outputs ]
                    fini { return() }
                }

                $addInputXacts()
                $addOutputXacts()
                $wipeInputsArray()
                $wipeOutputsArray()
            }
        }
        '''

        storm_crypto_lockout = '''
        model.deprecated.lock crypto:currency:transaction:inputs
        | model.deprecated.lock crypto:currency:transaction:outputs
        '''

        logger.debug('Making geo:name nodes from geo:place:name values.')
        opts = {'vars': {'layridens': layridens}}
        await self.runStorm(storm_geoplace_to_geoname, opts=opts)
        logger.debug('Update crypto:currency:transaction :input and :output property use.')
        await self.runStorm(storm_crypto_txin, opts=opts)
        logger.debug('Locking out crypto:currency:transaction :input and :output properties.')
        await self.runStorm(storm_crypto_lockout)

    async def runStorm(self, text, opts=None):
        '''
        Run storm code in a schedcoro and log the output messages.

        Args:
            text (str): Storm query to execute.
            opts: Storm opts.

        Returns:
            None
        '''
        async def _runStorm():
            async for mesgtype, mesginfo in self.core.storm(text, opts=opts):
                if mesgtype == 'print':
                    logger.debug(f'Storm message: {mesginfo.get("mesg")}')
                    continue
                if mesgtype == 'warn': # pragma: no cover
                    logger.warning(f'Storm warning: {mesginfo.get("mesg")}')
                    continue
                if mesgtype == 'err': # pragma: no cover
                    logger.error(f'Storm error: {mesginfo}')

        await self.core.schedCoro(_runStorm())

    async def revCoreLayers(self):

        version = self.revs[-1][0] if self.revs else maxvers

        # do a first pass to detect layers at the wrong version
        # that we are not able to rev ourselves and bail...

        layers = []
        for layr in self.core.layers.values():

            if layr.fresh:
                await layr.setModelVers(version)
                continue

            vers = await layr.getModelVers()
            if vers == version:
                continue

            if not layr.canrev and vers != version:
                mesg = f'layer {layr.__class__.__name__} {layr.iden} ({layr.dirn}) can not be updated.'
                raise s_exc.CantRevLayer(layer=layr.iden, mesg=mesg, curv=version, layv=vers)

            if vers > version:
                mesg = f'layer {layr.__class__.__name__} {layr.iden} ({layr.dirn}) is from the future!'
                raise s_exc.CantRevLayer(layer=layr.iden, mesg=mesg, curv=version, layv=vers)

            # realistically all layers are probably at the same version... but...
            layers.append(layr)

        # got anything to do?
        if not layers:
            return

        await self.core._enableMigrationMode()
        for revvers, revmeth in self.revs:

            todo = [lyr for lyr in layers if not lyr.ismirror and await lyr.getModelVers() < revvers]
            if not todo:
                continue

            logger.warning(f'beginning model migration -> {revvers}')

            await revmeth(todo)

            [await lyr.setModelVers(revvers) for lyr in todo]

        await self.core._disableMigrationMode()
        logger.warning('...model migrations complete!')
