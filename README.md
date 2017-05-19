# S3 Encrypt Resource for [Concourse CI](http://concourse.ci)

Resource to upload/download GPG encrypted files to S3. Unlike the [the official S3 Resource](https://github.com/concourse/s3-resource), this resource can upload or download multiple files using the `aws s3 sync` command.

## Usage

Include the following in your Pipeline YAML file, replacing the values in the angle brackets (`< >`):

```yaml
resource_types:
- name: <resource type name>
  type: docker-image
  source:
    repository: paasmule/s3-encrypt-resource
resources:
- name: <resource name>
  type: <resource type name>
  source:
    access_key_id: {{aws-access-key}}
    secret_access_key: {{aws-secret-key}}
    bucket: {{aws-bucket}}
    encryption_key: {{encryption_key}}
jobs:
- name: <job name>
  plan:
  - get: <resource name>
    params:
      path: <specific path from root the bucket>
      filter: <glob filter of files to get>    
  - <some Resource or Task that outputs files>
  - put: <resource name>
    params:
      path: <specific path from root the bucket>
      filter: <glob filter of files to put>
```

In case of [minio](https://www.minio.io/), add the following properties to your resource definition:

```yaml
resources:
- name: <resource name>
  type: <resource type name>
  source:
    ...
    endpoint: {{minio-endpoint-url}}
    use_v4: true
```

## AWS Credentials

The `access_key_id` and `secret_access_key` are optional and if not provided the EC2 Metadata service will be queried for role based credentials.

## Options

The `options` parameter is synonymous with the options that `aws cli` accepts for `sync`. Please see [S3 Sync Options](http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html#options) and pay special attention to the [Use of Exclude and Include Filters](http://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters).

Given the following directory `test`:

```
bosh-states
   ├── 1.json.gpg
   └── 2.json.gpg
scripts
    └── bad.sh
```

It is not necessary to specify the .gpg extension in the `filter` configuration.
We can download _only_ the -state.json files in `bosh-states` subdirectory by using the following `path` and `filter` in our task configuration:

```yaml
plan:
- do:
  - get: minio-s3
    params:
      path: bosh-states
      filter: "*-state.json"
```

Similarly, we can perform upload operations in the same fashion. As before, it is not necessary to worry about the .gpg extension on encypted files.

```yaml
ensure:
  put: minio-s3
  params:
    path: bosh-states
    filter: "*-state.json"
```
