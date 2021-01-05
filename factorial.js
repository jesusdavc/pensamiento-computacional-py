const factorial = (n) =>{
    if (n == 1){
        return 1
    }
    else{
        return n * factorial( n -1)
    }
}

let n = parseInt(prompt('Escriba un numero entero: '))

factorial(n)