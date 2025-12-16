"""
Message Processor

This module handles message processing and context management.
"""

import logging
from typing import Dict, List, Optional


logger = logging.getLogger(__name__)


class MessageProcessor:
    """
    Processes user messages and manages conversation context.
    """

    def __init__(self, agent, system_prompt: Optional[str] = None, max_context_messages: int = 10):
        """
        Initialize message processor.

        Args:
            agent: AI agent instance (e.g., DeepseekAgent)
            system_prompt: Default system prompt
            max_context_messages: Maximum number of messages to keep in context
        """
        self.agent = agent
        self.system_prompt = system_prompt or "You are a helpful AI assistant."
        self.max_context_messages = max_context_messages
        self.user_contexts: Dict[str, List[Dict[str, str]]] = {}

        logger.info("Message processor initialized")

    def process_message(self, user_id: str, message: str) -> str:
        """
        Process a user message and generate a response.

        Args:
            user_id: Unique user identifier
            message: User message text

        Returns:
            str: AI response
        """
        try:
            # Get or initialize user context
            context = self.user_contexts.get(user_id, [])

            # Generate response using the agent
            response = self.agent.generate_response(
                prompt=message,
                context=context,
                system_prompt=self.system_prompt
            )

            # Update context with new message and response
            self.update_context(user_id, message, response)

            return response

        except Exception as e:
            logger.error(f"Error processing message for user {user_id}: {e}")
            return "Sorry, I encountered an error while processing your message. Please try again."

    def update_context(self, user_id: str, user_message: str, ai_response: str):
        """
        Update conversation context for a user.

        Args:
            user_id: Unique user identifier
            user_message: User's message
            ai_response: AI's response
        """
        if user_id not in self.user_contexts:
            self.user_contexts[user_id] = []

        # Add user message and AI response to context
        self.user_contexts[user_id].append({"role": "user", "content": user_message})
        self.user_contexts[user_id].append({"role": "assistant", "content": ai_response})

        # Trim context if it exceeds max length
        if len(self.user_contexts[user_id]) > self.max_context_messages * 2:
            # Keep only the most recent messages
            self.user_contexts[user_id] = self.user_contexts[user_id][-(self.max_context_messages * 2):]

        logger.debug(f"Updated context for user {user_id}: {len(self.user_contexts[user_id])} messages")

    def clear_context(self, user_id: str):
        """
        Clear conversation context for a user.

        Args:
            user_id: Unique user identifier
        """
        if user_id in self.user_contexts:
            del self.user_contexts[user_id]
            logger.info(f"Cleared context for user {user_id}")

    def get_context(self, user_id: str) -> List[Dict[str, str]]:
        """
        Get conversation context for a user.

        Args:
            user_id: Unique user identifier

        Returns:
            List of message dictionaries
        """
        return self.user_contexts.get(user_id, [])
