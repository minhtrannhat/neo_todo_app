variable "github_token" {
  sensitive = true
}

provider "github" {
  token = var.github_token
}

resource "github_repository" "neo_todo_app" {
  name       = "neo_todo_app"
  visibility = "private"
}
