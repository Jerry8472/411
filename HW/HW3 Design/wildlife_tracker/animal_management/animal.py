from typing import Any, Optional

from wildlife_tracker.animal_management.animal import Animal
class Animal:
    def __init__(self,
                 age: Optional[int] = None,
                 animal_id: int = 0,
                 animals: dict[int, Animal] = {},
                 health_status: Optional[str] = None,
                 species: str = '') -> None:
        self.age = age 
        self.animal_id: animal_id
        self.animals: animals 
        self.health_status: health_status
        self.species: species
    
    def get_animal_details(animal_id) -> dict[str, Any]:
        pass
        
    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass
    pass
