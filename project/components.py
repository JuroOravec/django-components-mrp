import django_components

@django_components.register("a-outer-component")
class AOuterComponent(django_components.Component):
    template_file = "a-outer-component.html"

@django_components.register("b-inner-component")
class BInnerComponent(django_components.Component):
    template_file = "b-inner-component.html"
