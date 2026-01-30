use thiserror::Error;

#[derive(Error, Debug)]
pub enum RoStartError {
    #[error("System information error: {0}")]
    SystemInfo(String),

    #[error("Configuration error: {0}")]
    Config(#[from] anyhow::Error),

    #[error("IO error: {0}")]
    Io(#[from] std::io::Error),

    #[error("Command execution failed: {0}")]
    CommandFailed(String),

    #[error("Package manager not found")]
    PackageManagerNotFound,

    #[error("Update check failed: {0}")]
    UpdateCheckFailed(String),
}

pub type Result<T> = std::result::Result<T, RoStartError>;
