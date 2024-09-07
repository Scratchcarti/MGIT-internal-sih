from django import template

register = template.Library()

@register.filter

def space(application_status):

    return application_status.replace('-', ' ').title()

@register.filter
def crkt(name):

    if name == 'aadhaar':
        name = 'Aadhar Card'
        return name
    if name == 'income':
        name = 'Income Certificate'
        return name
    if name == 'caste':
        name = 'Caste Certificate'
        return name
    if name == 'domicile':
        name = 'Domicile Certificate'
        return name
    if name == 'tenth':
        name = '10th Certificate'
        return name
    if name == 'twelfth':
        name = '12th Certificate'
        return name

    else:
        return name