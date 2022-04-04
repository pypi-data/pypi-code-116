# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import boolean, integer
from .validators.waf import validate_waf_action_type


class FieldToMatch(AWSProperty):
    """
    `FieldToMatch <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html>`__
    """

    props: PropsDictType = {
        "Data": (str, False),
        "Type": (str, True),
    }


class ByteMatchTuples(AWSProperty):
    """
    `ByteMatchTuples <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "PositionalConstraint": (str, True),
        "TargetString": (str, False),
        "TargetStringBase64": (str, False),
        "TextTransformation": (str, True),
    }


class ByteMatchSet(AWSObject):
    """
    `ByteMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html>`__
    """

    resource_type = "AWS::WAF::ByteMatchSet"

    props: PropsDictType = {
        "ByteMatchTuples": ([ByteMatchTuples], False),
        "Name": (str, True),
    }


class IPSetDescriptors(AWSProperty):
    """
    `IPSetDescriptors <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html>`__
    """

    props: PropsDictType = {
        "Type": (str, True),
        "Value": (str, True),
    }


class IPSet(AWSObject):
    """
    `IPSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html>`__
    """

    resource_type = "AWS::WAF::IPSet"

    props: PropsDictType = {
        "IPSetDescriptors": ([IPSetDescriptors], False),
        "Name": (str, True),
    }


class Predicates(AWSProperty):
    """
    `Predicates <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html>`__
    """

    props: PropsDictType = {
        "DataId": (str, True),
        "Negated": (boolean, True),
        "Type": (str, True),
    }


class Rule(AWSObject):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html>`__
    """

    resource_type = "AWS::WAF::Rule"

    props: PropsDictType = {
        "MetricName": (str, True),
        "Name": (str, True),
        "Predicates": ([Predicates], False),
    }


class SizeConstraint(AWSProperty):
    """
    `SizeConstraint <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html>`__
    """

    props: PropsDictType = {
        "ComparisonOperator": (str, True),
        "FieldToMatch": (FieldToMatch, True),
        "Size": (integer, True),
        "TextTransformation": (str, True),
    }


class SizeConstraintSet(AWSObject):
    """
    `SizeConstraintSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html>`__
    """

    resource_type = "AWS::WAF::SizeConstraintSet"

    props: PropsDictType = {
        "Name": (str, True),
        "SizeConstraints": ([SizeConstraint], True),
    }


class SqlInjectionMatchTuples(AWSProperty):
    """
    `SqlInjectionMatchTuples <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformation": (str, True),
    }


class SqlInjectionMatchSet(AWSObject):
    """
    `SqlInjectionMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html>`__
    """

    resource_type = "AWS::WAF::SqlInjectionMatchSet"

    props: PropsDictType = {
        "Name": (str, True),
        "SqlInjectionMatchTuples": ([SqlInjectionMatchTuples], False),
    }


class Action(AWSProperty):
    """
    `Action <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html>`__
    """

    props: PropsDictType = {
        "Type": (validate_waf_action_type, True),
    }


class Rules(AWSProperty):
    """
    `Rules <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html>`__
    """

    props: PropsDictType = {
        "Action": (Action, False),
        "Priority": (integer, True),
        "RuleId": (str, True),
    }


class WebACL(AWSObject):
    """
    `WebACL <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html>`__
    """

    resource_type = "AWS::WAF::WebACL"

    props: PropsDictType = {
        "DefaultAction": (Action, True),
        "MetricName": (str, True),
        "Name": (str, True),
        "Rules": ([Rules], False),
    }


class XssMatchTuple(AWSProperty):
    """
    `XssMatchTuple <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html>`__
    """

    props: PropsDictType = {
        "FieldToMatch": (FieldToMatch, True),
        "TextTransformation": (str, True),
    }


class XssMatchSet(AWSObject):
    """
    `XssMatchSet <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html>`__
    """

    resource_type = "AWS::WAF::XssMatchSet"

    props: PropsDictType = {
        "Name": (str, True),
        "XssMatchTuples": ([XssMatchTuple], True),
    }
