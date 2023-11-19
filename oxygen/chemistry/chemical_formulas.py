from oxygen.chemistry.base import calculate_relative_molecular_mass


class ChemicalFormula:
    def __init__(self, elements: dict, formula: str,
                 name: str, molecular_mass: float=None):
        self.elements = elements
        self.formula = formula
        if molecular_mass is not None:
            self.molecular_mass = molecular_mass
        else:
            self.molucular_mass = calculate_relative_molecular_mass(formula, False)
        self.name = name


CHEMICAL_FORMULAS = {
    'H2O': ChemicalFormula({('H', 2), ('O', 1)}, "H2O", 'Вода', None)
}
