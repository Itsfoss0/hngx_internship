## Student API
This is a simple student rest API

## Usage

Clone this repo into your local machine

```
git clone https://github.com/Itsfoss0/hgnx_internship.git
```
Change directory to the one you just cloned

```
cd hngx_intership/0x0-rest_api/
```

Installed the requirements
```
pip3 install -r requirements.txt
```

Start the server and have fun

```
┌─[itsfoss@itsfoss]─[~/Desktop/hgnx_internship/0x0-rest_api]
└──╼ $python3 -m api.v1.app
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
```

```
┌─[itsfoss@itsfoss]─[~/Desktop/hgnx_internship/0x0-rest_api]
└──╼ $curl 0:5000/api/v1/status
{"status":"ok"}
┌─[itsfoss@itsfoss]─[~/Desktop/hgnx_internship/0x0-rest_api]
└──╼ $curl 0:5000/api/v1/student?slack_name=John%20Doe
{"current_day":"Thursday","github_file_url":"https://github.com/Itsfoss0/hgnx_internship/0x0-rest_api","github_repo":"https://github.com/Itsfoss0/hgnx_internship","slack_name":"John Doe","status_code":200,"track":"backend","utc_time":"2023-09-07T15:41:53Z"}
┌─[itsfoss@itsfoss]─[~/Desktop/hgnx_internship/0x0-rest_api]
└──╼
```
