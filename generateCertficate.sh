#!/bin/bash

# Read variables from env
source .env

# Create /cert_to_import folder if it does not exist
[[ -d cert_to_import ]] || mkdir cert_to_import

cd nginx

# Create /certs folder if it does not exist
[[ -d certs ]] || mkdir certs
cd certs

# Generate the CA
echo "Generating CA..."
openssl genrsa \
	-out ca.key \
	4096

openssl req -new -x509 \
	-days 365 \
	-sha256 \
	-subj "/C=${COUNTRY_CODE}/O=${COMPANY}/CN=${AUTHORITY_NAME}" \
	-key ca.key \
	-out ca.crt

# Generate server certificate
echo "Generating Server Certificate..."
openssl genrsa \
	-out server.key \
	4096

openssl req -new -sha256 \
	-subj "/CN=${COMMON_NAME}" \
	-key server.key \
	-out server.csr

echo "subjectAltName = DNS:${COMMON_NAME}" >extfile.cnf

openssl x509 -req \
	-days 365 \
	-sha256 \
	-in server.csr \
	-CA ca.crt -CAkey ca.key \
	-CAcreateserial -out server.crt \
	-extfile extfile.cnf
rm extfile.cnf
rm server.csr

# Generate client certificate
echo "Generating Client Certificate..."
openssl genrsa -out client.key 4096

openssl req -subj "/CN=client" -new -key client.key -out client.csr
echo "extendedKeyUsage = clientAuth" >extfile.cnf

openssl x509 -req \
	-days 365 \
	-sha256 \
	-in client.csr \
	-CA ca.crt -CAkey ca.key \
	-CAcreateserial -out client.crt \
	-extfile extfile.cnf
rm extfile.cnf
rm client.csr

# Copy client certificate to folder
cp client.* ../../cert_to_import/

echo "All done !"
echo "You can now copy the certificate and the key from the 'cert_to_import' folder to the reNgine server. \nBoth files go to the 'web/user-cert/<TARGET-NAME>' folder"
