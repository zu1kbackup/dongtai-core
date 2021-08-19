######################################################################
# @author      : bidaya0 (bidaya0@$HOSTNAME)
# @file        : translation
# @created     : Friday Aug 13, 2021 14:31:38 CST
#
# @description :
######################################################################


from modeltranslation.translator import translator, TranslationOptions, register
from dongtai.models.strategy import IastStrategyModel
from dongtai.models.vul_level import IastVulLevel
from dongtai.models.vulnerablity import IastVulnerabilityModel
from dongtai.models.deploy import IastDeployDesc
from dongtai.models.document import IastDocument
from dongtai.models.hook_type import HookType
from dongtai.models.department import Department
from dongtai.models.talent import Talent


@register(IastStrategyModel)
class IastStrategyModelTranslationOptions(TranslationOptions):
    fields = ('vul_name', 'vul_desc', 'vul_fix')


@register(IastVulLevel)
class IastVulLevelTranslationOptions(TranslationOptions):
    fields = ('name_value', 'name_type')


@register(IastDeployDesc)
class IastDeployDescTranslationOptions(TranslationOptions):
    fields = ('desc',)


@register(IastDocument)
class IastDocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'url')


@register(HookType)
class HookTypeTranslationOptions(TranslationOptions):
    fields = ('name',)