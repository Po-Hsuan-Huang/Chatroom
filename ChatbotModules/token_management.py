"""
Token Management Module

This module contains functions to manage token allocation among multiple agents.
"""

def allocate_token_budget(total_tokens, num_agents, current_usage):
    """
    Allocate and manage token usage across multiple agents.

    Args:
        total_tokens (int): The total number of tokens available (e.g., 128,000).
        num_agents (int): The number of agents in the conversation.
        current_usage (dict): A dictionary mapping each agent to their current token usage.

    Returns:
        dict: A dictionary mapping each agent to their allocated tokens.
    """
    allocation = {}
    remaining_tokens = total_tokens

    for agent in current_usage:
        if agent in current_usage:
            allocation[agent] = min(current_usage[agent], remaining_tokens // num_agents)
            remaining_tokens -= allocation[agent]
        else:
            allocation[agent] = remaining_tokens // num_agents

    return allocation
