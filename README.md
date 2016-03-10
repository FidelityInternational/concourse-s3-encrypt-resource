# Simple S3 Resource for [Concourse CI](http://concourse.ci)

Resource to upload files to S3. Unlike the [the official S3 Resource](https://github.com/concourse/s3-resource), this Resource doesn't care about files being versioned.

## Usage

TODO

## Development

Requires Docker.

```bash
cp .env.example .env

# modify .env

# exclude the `s3://` prefix/protocol for the `bucket`
./script/run </full/path/to/dir/or/file> <bucket>
```
