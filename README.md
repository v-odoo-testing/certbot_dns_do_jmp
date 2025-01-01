# DO VCT DNS Authenticator plugin for Certbot

A certbot DNS authenticator plugin for DigitalOcean DNS for another domain.

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
 # DigitalOcean API credentials used by Certbot
   dns_do_token = 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
```

### Obtaining Certificates

To obtain a certificate using this plugin:

```bash
certbot certonly \
  --authenticator dns-do-vct \
  --dns-do-credentials ~/.secrets/do.ini \
  --dns-do-jump-domain jump.domain \
  -d example.com
```

this requires a ~/.secrets/do.ini file with the following format:

```bash
# DigitalOcean API credentials used by Certbot
dns_do_token = 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
```

and a CNAME record on the target domain:

```bash
DNS Domain: example.com
TXT RECORD NAME: _acme-challenge
TXT RECORD VALUE: _acme-challenge-example-com.jump.domain
TXT RECORD TTL: 60
```


### Plugin Arguments

The following arguments are supported:

* `--dns-do-jump-domain jump.domain`: The domain to use for the CNAME record (Required)
* `--dns-do-vct-credentials`: Path to DigitalOcean credentials INI file (Required)
* `--dns-do-vct-propagation-seconds`: The number of seconds to wait for DNS to propagate before asking the ACME server to verify the DNS record (Default: 30)

## License

This plugin is licensed under the Apache License 2.0.
