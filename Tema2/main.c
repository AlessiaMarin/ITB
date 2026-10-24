#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

#include "merkle_tree.h"

int main(void) {
    printf("Hello, World!\n");
    MerkleTree *tree = create_merkle_tree();
    FILE *f = fopen("../students_2026.txt", "r");
    if (f == NULL) {
        perror("Could not open students_2026.txt");
        return 1;
    }

    char line[256];
    while (fgets(line, sizeof(line), f)) {
        line[strcspn(line, "\r\n")] = '\0';
        char *start = strchr(line, '"');
        char *end = strrchr(line, '"');
        if (start != NULL && end != start) {
            *end = '\0';
            start++;
        } else {
            start = line;
        }

        add_element(tree, start);
        // printf("Added: %s\n", start);
    }
    char my_name[] = "Marin Alessia";
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((const unsigned char *) my_name, strlen(my_name), hash);
    char *hex = hash_to_string(hash);
    printf("%s\n", hex);
    free(hex);

    if (find_element(tree, my_name))
        printf("Found: %s\n", my_name);
    else
        printf("Not found\n");


    MerkleProof *p = generate_proof(tree, "Marin Alessia");
    if (p == NULL) {
        printf("Not found\n");
    } else {
        printf("Checked %d parents:\n", get_proof_count(p));
        for (int i = 0; i < get_proof_count(p); i++) {
            char *s = hash_to_string(get_proof_sibling(p, i));
            printf("%d: %s\n", i, s);
            free(s);
        }
        if (verify_proof(get_root_hash(tree), "Marin Alessia", p)) {
            printf("Valid\n");
        } else {
            printf("Invalid\n");
        }
        free_merkle_proof(p);
    }

    return 0;
}
