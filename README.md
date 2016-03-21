# Simple S3 Resource for [Concourse CI](http://concourse.ci)

Resource to upload files to S3.

## Usage

Include the following in your Pipeline YAML file, replacing the values in the angle brackets (`< >`):

```yaml
resource_types:
- name: <resource type name>
  type: docker-image
  source:
    repository: 18fgsa/s3-resource-simple
resources:
- name: <resource name>
  type: <resource type name>
  source:
    access_key_id: {{aws-access-key}}
    secret_access_key: {{aws-secret-key}}
    bucket: {{aws-bucket}}
    options: [<optional, see note below>]
jobs:
- name: <job name>
  plan:
  - <some Resource or Task that outputs files>
  - put: <resource name>
```

### Options
The `options` parameter is synonymous with the options that `aws cli` accepts for `sync`. Please see [S3 Sync Options](http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html#options) and pay special attention to the [Use of Exclude and Include Filters](http://docs.aws.amazon.com/cli/latest/reference/s3/index.html#use-of-exclude-and-include-filters)

Given the following directory `test` we can upload _only_ the `results` subdirectory by using the `options` JSON below.

```
test
├── results
│   ├── 1.json
│   └── 2.json
└── scripts
    └── bad.sh
```
```
options:
  - "--exclude: '*'",
  - "--include: 'results/*'"
```

## Development

Requires [Docker](https://www.docker.com/).

### Building, Uploading, and Using the Docker Image
1. Download [Docker Toolbox](https://www.docker.com/products/docker-toolbox).
1. Get a [Docker Hub](https://www.dockerhub.com) account
1. Launch the Docker Terminal and `cd` to this directory.
1. `docker login -e <email> -p <password> -u <username>`
1. `docker build -t <username>/s3-resource-simple .`
1. verify with `docker images`
1. `docker push <username>/s3-resource-simple`
1. Now you can test your local Concourse pipelines using <username>/s3-resource-simple.


### Tests
1. Run `cp config.example.json config.json`.
1. Modify `config.json`.
  * See [the instructions for getting your AWS credentials](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup).
  * Recommended local S3 setup is via `cloud.gov`'s [s3 service and a Static app](https://docs.cloud.gov/apps/s3/).
  * Exclude the `s3://` prefix/protocol for `bucket`.

1. Run `./test/out </full/path/to/dir>`.
