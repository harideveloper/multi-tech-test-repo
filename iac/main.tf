terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.2"
    }
  }
}

resource "local_file" "example" {
  content  = "Hello from Terraform"
  filename = "${path.module}/hello.txt"
}
