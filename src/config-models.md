# Models

This section controls model selection and behavior. 

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>builtin</code></td>
    <td>Built-in model configurations</td>
</tr>
<tr>
    <td><code>custom</code></td>
    <td>Custom model configurations. Entries with the same name as a builtin will override the builtin</td>
</tr>
<tr>
    <td><code>default</code></td>
    <td>The default model name</td>
</tr>
<tr>
    <td><code>no_stream</code></td>
    <td>Disable streaming for all models</td>
</tr>
</table>


# Builtin models

Tenx auto-configures builtin models based on the presence of API keys in
environment variables:

<table>
<thead>
    <th>Environment Variable</th>
    <th>Models Added</th>
</thead>
<tr>
    <td><code>ANTHROPIC_API_KEY</code></td>
    <td>
        <code>sonnet</code> (claude-3-5-sonnet-latest)<br>
        <code>haiku</code> (claude-3-5-haiku-latest)
    </td>
</tr>
<tr>
    <td><code>DEEPINFRA_API_KEY</code></td>
    <td>
        <code>qwen</code> (Qwen/Qwen2.5-32B-Instruct)<br>
        <code>llama-8b-turbo</code> (meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo)<br>
        <code>llama-70b</code> (meta-llama/Meta-Llama-3.1-70B-Instruct)<br>
        <code>deepseek</code> (deepseek-ai/DeepSeek-V2.5)
    </td>
</tr>
<tr>
    <td><code>OPENAI_API_KEY</code></td>
    <td>
        <code>o1</code> (o1-preview)<br>
        <code>o1-mini</code> (o1-mini)<br>
        <code>gpt4o</code> (gpt-4o)<br>
        <code>gpt4o-mini</code> (gpt-4o-mini)
    </td>
</tr>
<tr>
    <td><code>XAI_API_KEY</code></td>
    <td>
        <code>grok</code> (grok-beta)
    </td>
</tr>
<tr>
    <td><code>GOOGLEAI_API_KEY</code></td>
    <td>
        <code>gemini</code> (gemini-exp-1114)
    </td>
</tr>
</table>


# Custom models

Models configurations come in two varieities - **claude**, which is specific to
the Anthropic API, and **openai**, which can be used for any model compatible
with the OpenAI API.

The possible fields for **claude** models are:

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>name</code></td>
    <td>The name used to refer to this model</td>
</tr>
<tr>
    <td><code>api_model</code></td>
    <td>The API model identifier</td>
</tr>
<tr>
    <td><code>key</code></td>
    <td>The API key</td>
</tr>
<tr>
    <td><code>key_env</code></td>
    <td>Environment variable to load the API key from if key is empty</td>
</tr>
</table>

The possible fields for **openai** models are:

<table>
<thead>
    <th>Field</th>
    <th>Description</th>
</thead>
<tr>
    <td><code>name</code></td>
    <td>The name of the model</td>
</tr>
<tr>
    <td><code>api_model</code></td>
    <td>The API model identifier</td>
</tr>
<tr>
    <td><code>key</code></td>
    <td>The API key</td>
</tr>
<tr>
    <td><code>key_env</code></td>
    <td>The environment variable to load the API key from</td>
</tr>
<tr>
    <td><code>api_base</code></td>
    <td>The base URL for the API</td>
</tr>
<tr>
    <td><code>can_stream</code></td>
    <td>Whether the model can stream responses</td>
</tr>
<tr>
    <td><code>no_system_prompt</code></td>
    <td>Whether the model supports a separate system prompt</td>
</tr>
</table>


# Example

Example of configuring a custom model using Ollama:

```ron
(
    models: (
        custom: [
            open_ai(
                name: "codellama",
                api_model: "codellama",
                key: "",  // Ollama doesn't need an API key
                key_env: "",
                api_base: "http://localhost:11434/v1",
                can_stream: true,
                no_system_prompt: false,
            ),
        ],
        default: "codellama",
    ),
)
```
