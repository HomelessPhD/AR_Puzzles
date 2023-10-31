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



    // PZL5 msg
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
