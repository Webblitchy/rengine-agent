# Rengine agent

## How to use
1. Run the script `generateCertficate.sh` to generate the certificate and the corresponding key.
2. In the reNgine web interface create a new "Internal Target"
3. Move the 2 generated files with the name of the target in <RENGINE_FOLDER>/web/user-certs/<TARGET_NAME>
4. Start the agent with the command `docker-compose build && docker-compose up` from the rengine-agent folder
5. Start a port scan from the web interface
