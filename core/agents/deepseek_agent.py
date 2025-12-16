"""
Deepseek AI Agent

This module provides an agent for interacting with the Deepseek API.
"""

import logging
from typing import Optional, Dict, List
import openai


logger = logging.getLogger(__name__)


class DeepseekAgent:
    """
    Agent for working with Deepseek API.

    Deepseek API is compatible with OpenAI API format.
    """

    def __init__(
        self,
        api_key: str,
        model: str = "deepseek-chat",
        base_url: str = "https://api.deepseek.com",
        max_tokens: int = 2000,
        temperature: float = 0.7
    ):
        """
        Initialize Deepseek agent.

        Args:
            api_key: Deepseek API key
            model: Model name (default: deepseek-chat)
            base_url: API base URL
            max_tokens: Maximum number of tokens in response
            temperature: Temperature for generation (0.0 - 2.0)
        """
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

        # Configure OpenAI client for Deepseek API
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        logger.info(f"Deepseek agent initialized with model: {model}")

    def generate_response(
        self,
        prompt: str,
        context: Optional[List[Dict[str, str]]] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """
        Generate response to a prompt.

        Args:
            prompt: User message
            context: Conversation history (list of messages)
            system_prompt: System prompt for the AI

        Returns:
            str: AI response
        """
        try:
            messages = []

            # Add system prompt if provided
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})

            # Add context if provided
            if context:
                messages.extend(context)

            # Add current user message
            messages.append({"role": "user", "content": prompt})

            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )

            # Extract response text
            ai_response = response.choices[0].message.content

            logger.info(f"Generated response: {len(ai_response)} characters")
            return ai_response

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            raise

    def stream_response(
        self,
        prompt: str,
        context: Optional[List[Dict[str, str]]] = None,
        system_prompt: Optional[str] = None
    ):
        """
        Generate streaming response to a prompt.

        Args:
            prompt: User message
            context: Conversation history
            system_prompt: System prompt for the AI

        Yields:
            str: Chunks of AI response
        """
        try:
            messages = []

            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})

            if context:
                messages.extend(context)

            messages.append({"role": "user", "content": prompt})

            stream = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stream=True
            )

            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content

        except Exception as e:
            logger.error(f"Error in streaming response: {e}")
            raise
