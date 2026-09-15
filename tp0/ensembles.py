""" retourne l'ensembles des robots effectuant les deux missions """
def robots_double_mission(robots_exploration, robots_transport):
    return robots_exploration & robots_transport
""" retourne l'ensembles des robots effectuant les missions """
def robots_toutes_missions(robots_exploration, robots_transport):
    return robots_exploration | robots_transport
""" retourne l'ensembles des robots effectuant que l'exploration """
def robots_exploration_seulement(robots_exploration, robots_transport):
    return robots_exploration - robots_transport

robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}


double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)
assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

"""fonction permettant d'ajouter un robot dans une mission"""
def ajouter_robots_mission(mission, robot):
    new_mission = set() #creation d'un nouveau ensemble
    new_mission = new_mission | mission # on recopie l'ensemble
    new_mission.add(robot) # ajout du robot
    return new_mission
    
def retirer_robot_mission(mission, robot):
    new_mission = set()
    new_mission = new_mission | mission
    new_mission.remove(robot) # suppression du robot
    return new_mission
    


ajout = ajouter_robots_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}