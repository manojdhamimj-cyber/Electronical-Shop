from django import template

register = template.Library()

@register.filter(name='npr')
def nepali_rs(value):
    """
    Converts a number/decimal to formatted Nepali Rupees (Rs. XX,XXX or NPR XX,XXX)
    """
    try:
        val = float(value)
        # Standard currency formatting with commas
        return f"Rs. {val:,.2f}"
    except (ValueError, TypeError):
        return f"Rs. {value}"
