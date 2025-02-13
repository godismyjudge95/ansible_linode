# ssh_key_info

Get info about the Linode SSH public key.

- [Examples](#examples)
- [Parameters](#parameters)
- [Return Values](#return-values)

## Examples

```yaml
- name: Get info about a SSH key by label
  linode.cloud.ssh_key_info:
    label: my-ssh-key
```

```yaml
- name: Get info about a SSH key by ID
  linode.cloud.ssh_key_info:
    id: 12345
```


## Parameters

| Field     | Type | Required | Description                                                                  |
|-----------|------|----------|------------------------------------------------------------------------------|
| `id` | <center>`int`</center> | <center>Optional</center> | The ID of the SSH key.  **(Conflicts With: `label`)** |
| `label` | <center>`str`</center> | <center>Optional</center> | The label of the SSH key.  **(Conflicts With: `id`)** |

## Return Values

- `ssh_key` - The SSH key in JSON serialized form.

    - Sample Response:
        ```json
        {
          "created": "2018-01-01T00:01:01",
          "id": 42,
          "label": "My SSH Key",
          "ssh_key": "ssh-rsa AAAA_valid_public_ssh_key_123456785== user@their-computer"
        }
        ```
    - See the [Linode API response documentation](https://www.linode.com/docs/api/profile/#ssh-key-view__response-samples) for a list of returned fields


