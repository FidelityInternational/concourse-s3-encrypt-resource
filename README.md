# Simple S3 Resource for [Concourse CI](http://concourse.ci)

Resource to upload files to S3. Unlike the [the official S3 Resource](https://github.com/concourse/s3-resource), this Resource doesn't care about files being versioned.

## Usage

TODO

## Development

Requires Docker.

1. Run `cp config.example.json config.json`.
1. Modify `config.json`.
    * See [the instructions for getting your AWS credentials](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup).
    * Exclude the `s3://` prefix/protocol for the `bucket`.
1. Run `./test/run </full/path/to/dir/or/file>`.
