# OOP Battle Simulation Engine

A robust Python simulation demonstrating advanced Object-Oriented Programming (OOP) concepts. The project models a scalable entity interaction system ("Battle Arena") using strict design patterns relevant to verification and hardware modeling environments.

## Core Technical Concepts
This project was designed to practice and demonstrate:
* **Polymorphism & Inheritance:** Implemented a multi-layer class hierarchy (`Pokemon` ABC -> `Attributes` -> `Elemental Type` -> `Specific Implementation`) allowing for modular expansion.
* **Encapsulation:** Strict usage of private members (e.g., `__hit_points`) and public interfaces to protect entity state from invalid modifications.
* **Abstract Base Classes (ABC):** Utilized Python's `abc` module to enforce design contracts and standardize interfaces across all derived classes.
* **State Management:** Developed a turn-based logic engine (`Battle.py`) that manages simulation flow, round counting, and win/loss conditions efficiently.

## File Structure
* `Pokemon.py`: Defines the Abstract Base Class (Interface) and core logic shared by all entities.
* `Battle.py`: The main simulation engine managing the interaction logic between objects.
* `[Type].py` (Fire.py/Water.py/Electric.py): Intermediate classes implementing specific elemental attributes.
