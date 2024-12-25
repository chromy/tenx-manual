use misanthropy::{
    Anthropic, Content, Message, MessagesRequest, Result, Role, Text, ANTHROPIC_API_KEY_ENV,
    DEFAULT_MAX_TOKENS, DEFAULT_MODEL,
};
use tokio;

#[tokio::main]
async fn main() -> Result<()> {
    let api_key = std::env::var(ANTHROPIC_API_KEY_ENV).expect("API key not found in environment");

    let client = Anthropic::new(&api_key);
    let request = MessagesRequest {
        model: DEFAULT_MODEL.to_string(),
        max_tokens: DEFAULT_MAX_TOKENS,
        messages: vec![Message {
            role: Role::User,
            content: vec![Content::Text(Text::new("How do you feel?"))],
        }],
        ..Default::default()
    };

    let response = client.messages(&request).await?;
    println!("{}", response.format_content());

    Ok(())
}
