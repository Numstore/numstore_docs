// Placeholder header file for Numstore C library
// Replace with actual header file

#ifndef NUMSTORE_H
#define NUMSTORE_H

typedef struct numstore_connection numstore_connection;

// Connect to Numstore database
numstore_connection* ns_connect(const char* host, int port);

// Close connection
void ns_close(numstore_connection* conn);

#endif // NUMSTORE_H
