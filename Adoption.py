import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name=name
        self.location=location
        self.species_types=species_types
    def get_number_of_species(self, animal):
        return self.species_types.get(animal, 0)
    def get_location(self):
        return float(self.location)
    def get_species_count(self):
        spec = self.species_types.copy()
        for i in self.species_types:
            if self.species_types.get(i, 0) == 0:
                del spec[i]
        self.species_types = spec.copy()
        return spec.copy()
    def get_name(self):
        return self.name 
    def adopt_pet(self, species):
        if not (self.species_types.get(species, 0 ) == 0):
            self.species_types[species]=self.species_types[species]-1

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name=name
        self.desired_species=desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species 
    def get_score(self, adoption_center):
        return float(adoption_center.get_number_of_species(self.desired_species))

class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species=considered_species
    def get_score(self, adoption_center):
        tot = float(adoption_center.get_number_of_species(self.desired_species))
        for i in self.considered_species:
            tot = tot + (0.3 * float(adoption_center.get_number_of_species(i)))
        return tot

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species=feared_species
    def get_score(self, adoption_center):
        tot = float(adoption_center.get_number_of_species(self.desired_species)) - (0.3 * float(adoption_center.get_number_of_species(self.feared_species)))
        if tot<0:
            return float(0)
        return tot
    
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species=allergic_species
    def get_score(self, adoption_center):
        for i in self.allergic_species:
            if i in adoption_center.get_species_count():
                return float(0)
        else:
            return float(adoption_center.get_number_of_species(self.desired_species))

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness=medicine_effectiveness
    def get_score(self, adoption_center):
        low = 1
        for j in self.medicine_effectiveness:
            if j in adoption_center.get_species_count():
                if self.medicine_effectiveness[j]<low:
                    low=self.medicine_effectiveness[j]
        tot = low*float(adoption_center.get_number_of_species(self.desired_species))
        return tot
        
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    # Your Code Here, should contain an __init__ and a get_score method.
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location=location
    def get_linear_distance(self, to_location):
        loc = self.location
        d = (float(to_location[0]-loc[0])**2) + (float(to_location[1]-loc[1])**2)
        return d**0.5
    def get_score(self, adoption_center):
        d = self.get_linear_distance(adoption_center.get_location())
        tot = float(adoption_center.get_number_of_species(self.desired_species))
        if d<1:
            return tot
        elif 3>d>=1:
            return random.uniform(.7,0.9)*tot
        elif 5>d>=3:
            return random.uniform(0.5,0.7)*tot
        else:
            return random.uniform(0.1,0.5)*tot

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here
    list1=[]
    for i in list_of_adoption_centers:
        list1.append(adopter.get_score(i))
    list1.sort(reverse=True)
    List=[]
    for e in list_of_adoption_centers :
        List.append((adopter.get_score(e),e))
    List.sort(reverse=True)
    for i,j in enumerate(List):
        if i<len(List):
            if List[i][0]==List[i+1][0]:
                if j>List[i+1][1]:
                    temp=List[i]
                    List[i]=List[i+1]
                    List[i+1]=temp
    L2=[]
    for e in List:
        L2.append(e[1])
    return L2
        

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 

