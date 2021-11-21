from principle.solid.ocp.good.Specification import Specification
from principle.solid.ocp.good.ColorSpecification import ColorSpecification
from principle.solid.ocp.good.SizeSpecification import SizeSpecification

if __name__ == '__main__':
    print(issubclass(ColorSpecification, Specification))
    print(issubclass(SizeSpecification, Specification))
