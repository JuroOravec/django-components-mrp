import django_components

@django_components.register("a-outer-component")
class AOuterComponent(django_components.Component):
    template = """
    {% load component_tags %}
    <div>
        <p>This is the outer component.</p>
        {% slot "a" default / %}
    </div>
    """

@django_components.register("b-inner-component")
class BInnerComponent(django_components.Component):
    template = """
    {% load component_tags %}
    <div>
        <p>This is the inner component.</p>
        {% slot "b" default / %}
    </div>
    """
