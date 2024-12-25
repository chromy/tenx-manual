use misanthropy::{Anthropic, Content, Message, MessagesRequest, Role};
use std::env;

#[tokio::main]
async fn main() {
    // Read API key from the environment
    let api_key = env::var("ANTHROPIC_API_KEY").expect("API key not found in environment");

    // Create a new Anthropic client
    let client = Anthropic::new(&api_key);

    // Create a new message request
    let request = MessagesRequest {
        model: misanthropy::DEFAULT_MODEL.to_string(),
        max_tokens: 50,
        messages: vec![Message {
            role: Role::User,
            content: vec![Content::Text(misanthropy::Text::new("How do you feel?"))],
        }],
        ..Default::default()
    };

    // Send the request to the API and await the response
    match client.messages(&request).await {
        Ok(response) => {
            for content in response.content {
                if let Content::Text(text) = content {
                    println!("{}", text.text);
                }
            }
        }
        Err(err) => eprintln!("Error: {:?}", err),
    }
}
