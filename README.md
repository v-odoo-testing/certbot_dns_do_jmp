vctdns DNS Authenticator plugin for Certbot

# vctdns DNS Authenticator plugin for Certbot

A certbot DNS authenticator plugin for DigitalOcean DNS.

## Installation

```bash
pip install certbot-dns-do-vct
```

## Usage

To use this plugin, you need to:

1. Create a DigitalOcean API token with read and write access
2. Configure the credentials file with your token
3. Run certbot with the plugin

### Credentials

Save your DigitalOcean API credentials to a file (e.g. `~/do-credentials.ini`) with the following format:

```bash
certbot certonly --authenticator dns-do-vct --dns-do-credentials ~/.secrets/certbot/do.ini --dns-do-jump-domain jump.domain -d example.com
```

### Obtaining Certificates

To obtain a certificate using this plugin:

```bash
certbot certonly --authenticator dns-do-vct --dns-do-credentials ~/.secrets/certbot/do.ini --dns-do-jump-domain jump.domain -d example.com
```

### Plugin Arguments

The following arguments are supported:

* `--dns-do-vct-credentials`: Path to DigitalOcean credentials INI file (Required)
* `--dns-do-vct-propagation-seconds`: The number of seconds to wait for DNS to propagate before asking the ACME server to verify the DNS record (Default: 30)

## License

This plugin is licensed under the Apache License 2.0.
