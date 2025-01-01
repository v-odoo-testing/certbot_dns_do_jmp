"""
The `~certbot_dns_do_vct.dns_do_vct` plugin automates the process of
completing a ``dns-01`` challenge by creating, and subsequently removing, TXT records using
the DigitalOcean API with a jump domain approach by adding a CNAME record for the target domain `_acme-challenge.example.com` pointing to`_acme-challenge.example.com`
pointing to `_acme-challenge-example-com.jump.domain`, where `jump.domain` is the jump domain specified in the plugin configuration.

In this way we can authenticate with unknown dns servers with our digital ocean domain as a jump domain.

.. note::
   The plugin is not installed by default. It can be installed using pip:

   ``pip install certbot-dns-do-vct``

Named Arguments
--------------

========================================  =====================================
``--dns-do-credentials``                  DigitalOcean credentials_ INI file.
                                         (Required)
``--dns-do-jump-domain``                 Jump domain for DNS validation.
                                         (Required)
``--dns-do-propagation-seconds``         The number of seconds to wait for DNS
                                         to propagate before asking the ACME
                                         server to verify the DNS record.
                                         (Default: 10)
========================================  =====================================


Credentials
----------

Use of this plugin requires a configuration file containing DigitalOcean API
credentials, obtained from your DigitalOcean account.

.. code-block:: ini
   :name: credentials.ini
   :caption: Example credentials file:

   # DigitalOcean API credentials used by Certbot
   dns_do_token = 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef

DNS Validation Process
--------------------

The plugin uses a "jump domain" approach for DNS validation:

1. For a target domain (e.g., example.com), the plugin will create a TXT record on the jump domain
   in the format: ``_acme-challenge-example-com.jump.domain``

2. You need to create a CNAME record on your target domain:
   ``_acme-challenge.example.com`` → ``_acme-challenge-example-com.jump.domain``

Examples
--------

.. code-block:: bash

   certbot certonly \\
     --authenticator dns-do-vct \\
     --dns-do-credentials ~/.secrets/do.ini \\
     --dns-do-jump-domain jump.domain \\
     -d example.com
"""

