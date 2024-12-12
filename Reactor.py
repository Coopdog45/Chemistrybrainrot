import IPython.display as ipd

class ChemicalReactionPredictor:
   def __init__(self):
      self.PERIODIC_TABLE_LAYOUT = [
        ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
        ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
        ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
        ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
        ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"]
      ]

      self.CHARGES = {
        "H": 1, "He": 0, "Li": 1, "Be": 2, "B": 3, "C": 4, "N": -3, "O": -2, "F": -1, "Ne": 0,
        "Na": 1, "Mg": 2, "Al": 3, "Si": 4, "P": -3, "S": -2, "Cl": -1, "Ar": 0,
        "K": 1, "Ca": 2, "Sc": 3, "Ti": 4, "V": 5, "Cr": 3, "Mn": 2, "Fe": 3, "Co": 2, "Ni": 2,
        "Cu": 2, "Zn": 2, "Ga": 3, "Ge": 4, "As": -3, "Se": -2, "Br": -1, "Kr": 0,
        "Rb": 1, "Sr": 2, "Y": 3, "Zr": 4, "Nb": 5, "Mo": 6, "Tc": 7, "Ru": 8,
        "Rh": 3, "Pd": 2, "Ag": 1, "Cd": 2, "In": 3, "Sn": 4, "Sb": -3, "Te": -2, "I": -1, "Xe": 0
      }

      self.AUDIO_FILES = {
        "Element + Element to Compound": "https://drive.google.com/file/d/1Z2ZEdL-Jpu-7Z2hpvBXEYZcUGl1RsUEd/view?usp=drive_link",
        "Compound to Element + Element": "https://example.com/Skib.mp3",
        "Compound + Compound to One Compound": "https://example.com/cookie.mp3",
        "Compound + Compound to Compound + Compound": "https://example.com/Two-Man.mp3",
        "Element + Compound to Element + Compound": "https://example.com/sigma.mp3",
        "Compound + Element to Compound + Compound": "https://example.com/ninja.mp3",
        "Compound to Compound + Element": "https://drive.google.com/file/d/16GqmZ8JAZ-X0HztoCLk7gvHjdNL6wsdD/view?usp=drive_link"
      }

   def predict_reaction(self, reactant1, reactant2, type1, type2):
      if type1 == "Element" and type2 == "Element":
        return "Element + Element to Compound"
      elif type1 == "Compound" and type2 == "None" or type1 == "None" and type2 == "Compound":
        if self.is_decomposition_to_compound_and_element(reactant1 if type1 == "Compound" else reactant2):
           return "Compound to Compound + Element"
        elif self.is_polyatomic_ion(reactant1 if type1 == "Compound" else reactant2):
           return "Compound to Element + Element"
        else:
           return "Compound to Element + Element"
      elif type1 == "Compound" and type2 == "Compound":
        if self.is_combination_reaction(reactant1, reactant2):
           return "Compound + Compound to One Compound"
        else:
           return "Compound + Compound to Compound + Compound"
      elif type1 == "Element" and type2 == "Compound" or type1 == "Compound" and type2 == "Element":
        if self.is_single_displacement_reaction(reactant1, reactant2):
           return "Element + Compound to Element + Compound"
        else:
           return "Compound + Element to Compound + Compound"

   def is_combination_reaction(self, reactant1, reactant2):
      combination_reactions = [("H2", "O2"), ("CO2", "H2O"), ("NaOH", "HCl")]
      return (reactant1, reactant2) in combination_reactions or (reactant2, reactant1) in combination_reactions

   def is_single_displacement_reaction(self, reactant1, reactant2):
      single_displacement_reactions = [("Na", "HCl"), ("Zn", "CuSO4"), ("Mg", "CuSO4")]
      return (reactant1, reactant2) in single_displacement_reactions or (reactant2, reactant1) in single_displacement_reactions

   def is_decomposition_to_compound_and_element(self, compound):
      decomposition_reactions = ["CaCO3"]
      return compound in decomposition_reactions

   def is_polyatomic_ion(self, compound):
      polyatomic_ions = ["NO3", "SO4", "PO4"]
      return compound in polyatomic_ions

   def play_audio(self, reaction_type):
      audio_url = self.AUDIO_FILES.get(reaction_type, "https://example.com/no_reaction.mp3")
      ipd.Audio(url=audio_url, autoplay=True)

   def run(self):
      reactant1 = input("Enter the first reactant: ")
      reactant2 = input("Enter the second reactant: ")
      type1 = input("Enter the type of the first reactant (Element or Compound): ")
      type2 = input("Enter the type of the second reactant (Element or Compound): ")

      reaction_type = self.predict_reaction(reactant1, reactant2, type1, type2)
      print("Reaction Type:", reaction_type)
      self.play_audio(reaction_type)

if __name__ == "__main__":
   predictor = ChemicalReactionPredictor()
   predictor.run()
