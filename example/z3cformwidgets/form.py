from plone.autoform.form import AutoExtensibleForm
from plone.autoform.interfaces import WIDGETS_KEY
from zope import interface
from zope import schema
from z3c.form import form

class FormSchema(interface.Interface):
    """Form schema"""
    textline = schema.TextLine(title=u"Text Line",
                               required=False)
    asciiline = schema.ASCIILine(title=u"ASCII Line",
                               required=False)
    text = schema.Text(title=u"Text",
                               required=False)
    ascii = schema.ASCII(title=u"ASCII",
                               required=False)
    
    int = schema.Int(title=u"Int",
                               required=False)
    float = schema.Float(title=u"Float",
                               required=False)
    bool = schema.Bool(title=u"Bool",
                               required=False)

    list_asciiline = schema.List(title=u"List of asciiline",
                           value_type=schema.ASCIILine(title=u"ASCIILine"),
                               required=False)

    color = schema.TextLine(title=u"Color",
                            required=False)
#    alphacolor = schema.TextLine(title=u"Color with alpha layer support",
#                                 required=False)

FormSchema.setTaggedValue(WIDGETS_KEY, {'color':'collective.z3cform.colorpicker.colorpicker.ColorpickerFieldWidget',
                                        'alphacolor':'collective.z3cform.colorpicker.colorpicker.ColorpickerAlphaFieldWidget'})

class Form(AutoExtensibleForm, form.Form):
    schema = FormSchema
    ignoreContext = True
