"""
Context Management Module

This module contains functions to summarize and prune conversation history to maintain relevant context.
"""

def summarize_and_prune_context(conversation_history, max_tokens):
    """
    Summarize and prune older parts of the conversation to maintain relevant context.

    Args:
        conversation_history (list): List of conversation segments.
        max_tokens (int): Maximum allowed tokens in the context (e.g., 128,000).

    Returns:
        list: Pruned conversation history that fits within the token limit.
    """
    pruned_history = []
    current_tokens = 0

    for segment in reversed(conversation_history):
        segment_tokens = len(segment.split())
        if current_tokens + segment_tokens <= max_tokens:
            pruned_history.insert(0, segment)
            current_tokens += segment_tokens
        else:
            break

    return pruned_history
