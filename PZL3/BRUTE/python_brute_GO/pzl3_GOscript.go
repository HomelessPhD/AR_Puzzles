package main

/*
To use this program you should remove two "condition" lines in a file $GOROOT/src/crypto/aes/cipher_asm.go:
	--- if !supportsAES {
          return newCipherGeneric(key)
	--- }

and change "case" line in a file $GOROOT/src/crypto/aes/cipher.go:

	func NewCipher(key []byte) (cipher.Block, error) {
	...
	--- case 16, 24, 32:
	+++ case 16, 24, 32, 128:
	...
	}

*/

import (
	"fmt"
	"encoding/hex"
	"crypto/sha512"
	"os"
	"hash"
	"strings"
	"crypto/aes"
	"crypto/cipher"
	"crypto/md5"
	"encoding/base64"
	"errors"	
	"bufio"
 )

var pz_salt []byte
var pz_cipherBytes []byte
var pz_cipherBytesLen int



    // PZL3 msg
const msg = "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"


func TiamatDecodeCheck(hasher hash.Hash, pass string) string {
	r := sha512.Sum512([]byte(pass))
	
	for in := 0; in < 11512; in++ {
	r = sha512.Sum512(r[:])
	}
	pwd := make([]byte, hex.EncodedLen(64))
	hex.Encode(pwd, r[:])
	derivedKeyBytes := []byte{}
	bx := []byte{}
	for len(derivedKeyBytes) < 144 {
		if len(bx) > 0 {
			hasher.Write(bx)
		}
		hasher.Write(pwd)
		hasher.Write(pz_salt)
		bx = hasher.Sum(nil)
		hasher.Reset()

		for i := 1; i < 10000; i++ {
			hasher.Write(bx)
			bx = hasher.Sum(nil)
			hasher.Reset()
		}
		derivedKeyBytes = append(derivedKeyBytes, bx...)
	}
	block, err := aes.NewCipher(derivedKeyBytes[:128])
	if err != nil {
		panic(err)
	}
	var cp []byte = make([]byte, pz_cipherBytesLen)
	copy(cp, pz_cipherBytes)
	mode := cipher.NewCBCDecrypter(block, derivedKeyBytes[128:])
	mode.CryptBlocks(cp, cp)
	length := len(cp)
	unpadding := int(cp[length-1])
	endp := string(cp[:(length - unpadding)])

	const search = "\"kty\":\"RSA\""

	if x := strings.Contains(endp, search); x == true {
            return "1"
	} else {
	    return "0"
	}
}

func b64toBinary() {
	data, err := base64.StdEncoding.DecodeString(msg)
	if err != nil {
	panic(errors.New("base64 invalid"))
	}
	if string(data[:8]) != "Salted__" {
		panic(errors.New("Invalid data"))
	}
	pz_salt = data[8:16]
	pz_cipherBytes = data[16:]
	pz_cipherBytesLen = len(pz_cipherBytes)
}

func main() {
    b64toBinary()
    h := md5.New()

    scanner := bufio.NewScanner(os.Stdin)
    var result string
    for scanner.Scan() {
        arg := scanner.Text()
        result += TiamatDecodeCheck(h,arg)
    }

    fmt.Println(result)

}
