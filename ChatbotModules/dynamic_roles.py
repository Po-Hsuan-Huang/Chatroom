"""
Dynamic Roles Module

This module contains functions to dynamically adjust agents' roles based on conversation flow.
"""

def adjust_roles_dynamically(current_roles, conversation_flow):
    """
    Dynamically adjust agents' roles based on conversation flow.

    Args:
        current_roles (dict): Current roles assigned to each agent.
        conversation_flow (list): Recent segments of the conversation.

    Returns:
        dict: Updated roles for each agent based on the conversation.
    """
    updated_roles = current_roles.copy()
    # Example logic for dynamic role adjustment
    for segment in conversation_flow:
        if "complex discussion" in segment:
            for agent in updated_roles:
                updated_roles[agent] = "leader" if "leader" in segment else "participant"
        elif "simple question" in segment:
            for agent in updated_roles:
                updated_roles[agent] = "expert" if "expert" in segment else "assistant"
    return updated_roles
