use misanthropy::{Anthropic, Content, Message, MessagesRequest, Role};

#[tokio::main]
async fn main() {
    // Create the Anthropic client using the API key from the environment
    let client = Anthropic::from_env().expect("Failed to create Anthropic client");

    // Create a new message
    let user_message = Message {
        role: Role::User,
        content: vec![Content::Text(misanthropy::Text {
            text: "How do you feel?".into(),
            cache_control: None,
        })],
    };

    // Create a request with the message
    let request = MessagesRequest {
        model: misanthropy::DEFAULT_MODEL.into(),
        max_tokens: 100,
        messages: vec![user_message],
        system: Vec::new(),
        temperature: None,
        stream: false,
        tools: Vec::new(),
        tool_choice: misanthropy::ToolChoice::Auto,
        stop_sequences: Vec::new(),
    };

    // Send the message request and capture the response
    match client.messages(&request).await {
        Ok(response) => {
            // Format and print the AI response
            println!("Claude: {}", response.format_content());
        }
        Err(e) => {
            eprintln!("Failed to get a response: {:?}", e);
        }
    }
}
