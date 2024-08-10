"""
Turn Management Module

This module contains functions to regulate turn-taking among agents.
"""

def manage_turn_taking(agent_responses, priority_rules):
    """
    Regulate turn-taking among agents.

    Args:
        agent_responses (dict): Dictionary of agents and their respective responses.
        priority_rules (dict): Rules that determine the priority of each agent.

    Returns:
        str: The agent selected to speak next.
    """
    sorted_agents = sorted(agent_responses.keys(), key=lambda agent: priority_rules.get(agent, 0), reverse=True)
    return sorted_agents[0] if sorted_agents else None
