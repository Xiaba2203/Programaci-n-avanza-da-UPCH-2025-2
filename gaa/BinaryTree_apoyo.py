# ==============================================================
# BinaryTree_apoyo.py  -  FUNCIONES DE APOYO PARA ARBOLES BINARIOS (BST)
# ==============================================================
# COMO USAR:   from BinaryTree_apoyo import *
#
# Todas las funciones reciben el ARBOL como primer parametro:
#       altura(mi_arbol)
# y leen la raiz con arbol.get_root() (o arbol.root).
#
# Casi todo se resuelve con RECURSION, siempre con el mismo esqueleto:
#       def f(nodo):
#           if nodo is None:        # CASO BASE (arbol vacio)
#               return ...
#           ... usar nodo.element, f(nodo.left), f(nodo.right)
#
# Reglas de un BST:  izquierda < nodo < derecha.
# Nada de listas de Python: los resultados se devuelven en LinkedList.
#
# Necesita en la misma carpeta: BinaryTree.py, LinkedList.py,
# LinkedList_apoyo.py y PilaCola_apoyo.py
# (renombra tu "BinaryTree (1).py" a BinaryTree.py si hace falta).
# ==============================================================

from BinaryTree import BinaryTree, TreeNode
from LinkedList import LinkedList
from LinkedList_apoyo import elementoEnPosicion, posicionDeElemento
from PilaCola_apoyo import Pila, Cola


# ==============================================================
# 1. RECORRIDOS QUE DEVUELVEN UNA LinkedList
# ==============================================================
# Tu clase ya trae inorder(), preorder(), postorder() que IMPRIMEN.
# Estas versiones los GUARDAN en una LinkedList para poder usarlos.
#
#   INORDER   : izquierda, RAIZ, derecha   -> sale ORDENADO de menor a mayor
#   PREORDER  : RAIZ, izquierda, derecha   -> la raiz va primero
#   POSTORDER : izquierda, derecha, RAIZ   -> la raiz va al final
#   NIVELES   : nivel por nivel, de izquierda a derecha (usa Cola)

def inorderLista(arbol):
    resultado = LinkedList()
    _inorder(arbol.get_root(), resultado)
    return resultado

def _inorder(nodo, resultado):
    if nodo is not None:
        _inorder(nodo.left, resultado)
        resultado.addLast(nodo.element)       # visito la raiz ENTRE los hijos
        _inorder(nodo.right, resultado)


def preorderLista(arbol):
    resultado = LinkedList()
    _preorder(arbol.get_root(), resultado)
    return resultado

def _preorder(nodo, resultado):
    if nodo is not None:
        resultado.addLast(nodo.element)       # visito la raiz ANTES
        _preorder(nodo.left, resultado)
        _preorder(nodo.right, resultado)


def postorderLista(arbol):
    resultado = LinkedList()
    _postorder(arbol.get_root(), resultado)
    return resultado

def _postorder(nodo, resultado):
    if nodo is not None:
        _postorder(nodo.left, resultado)
        _postorder(nodo.right, resultado)
        resultado.addLast(nodo.element)       # visito la raiz DESPUES


def porNivelesLista(arbol):
    """Recorrido por niveles (BFS). La cola guarda los nodos pendientes."""
    resultado = LinkedList()
    if arbol.get_root() is None:
        return resultado
    cola = Cola()
    cola.enqueue(arbol.get_root())
    while not cola.isEmpty():
        nodo = cola.dequeue()
        resultado.addLast(nodo.element)
        if nodo.left is not None:
            cola.enqueue(nodo.left)
        if nodo.right is not None:
            cola.enqueue(nodo.right)
    return resultado


# ==============================================================
# 2. RECORRIDOS ITERATIVOS (sin recursion, con Pila) - imprimen
# ==============================================================

def inorderIterativo(arbol):
    """Bajo todo a la izquierda apilando; al volver, imprimo y voy a la derecha."""
    pila = Pila()
    actual = arbol.get_root()
    while actual is not None or not pila.isEmpty():
        while actual is not None:
            pila.push(actual)
            actual = actual.left
        actual = pila.pop()
        print(actual.element, end=" ")
        actual = actual.right


def preorderIterativo(arbol):
    """Apilo primero el derecho para que el izquierdo salga antes."""
    if arbol.get_root() is None:
        return
    pila = Pila()
    pila.push(arbol.get_root())
    while not pila.isEmpty():
        nodo = pila.pop()
        print(nodo.element, end=" ")
        if nodo.right is not None:
            pila.push(nodo.right)
        if nodo.left is not None:
            pila.push(nodo.left)


def postorderIterativo(arbol):
    """Con dos pilas: la segunda recibe los nodos al reves y al vaciarla
    salen en postorder."""
    if arbol.get_root() is None:
        return
    pila1 = Pila()
    pila2 = Pila()
    pila1.push(arbol.get_root())
    while not pila1.isEmpty():
        nodo = pila1.pop()
        pila2.push(nodo)
        if nodo.left is not None:
            pila1.push(nodo.left)
        if nodo.right is not None:
            pila1.push(nodo.right)
    while not pila2.isEmpty():
        print(pila2.pop().element, end=" ")


# ==============================================================
# 3. POSICION DE UN ELEMENTO SEGUN EL RECORRIDO
# ==============================================================

def posicionInorder(arbol, e):
    """Posicion de e en el recorrido inorder (0 = el menor). -1 si no existe."""
    return posicionDeElemento(inorderLista(arbol), e)

def posicionPreorder(arbol, e):
    return posicionDeElemento(preorderLista(arbol), e)

def posicionPostorder(arbol, e):
    return posicionDeElemento(postorderLista(arbol), e)

def elementoEnPosicionInorder(arbol, k):
    """Elemento en la posicion k del inorder = el (k+1)-esimo menor."""
    return elementoEnPosicion(inorderLista(arbol), k)


# ==============================================================
# 4. BUSCAR NODOS Y RELACIONES (padre, hermano, hijos...)
# ==============================================================

def buscarNodo(arbol, e):
    """Devuelve el NODO que contiene e (None si no existe). Es un search
    que devuelve el nodo en vez de True/False."""
    actual = arbol.get_root()
    while actual is not None:
        if e < actual.element:
            actual = actual.left
        elif e > actual.element:
            actual = actual.right
        else:
            return actual
    return None


def padre(arbol, e):
    """Elemento PADRE de e (None si e es la raiz o no existe)."""
    anterior = None
    actual = arbol.get_root()
    while actual is not None:
        if e < actual.element:
            anterior = actual
            actual = actual.left
        elif e > actual.element:
            anterior = actual
            actual = actual.right
        else:
            if anterior is None:
                return None                   # es la raiz
            return anterior.element
    return None                               # no existe


def hermano(arbol, e):
    """Elemento HERMANO de e (el otro hijo de su padre). None si no tiene."""
    nodoPadre = None
    actual = arbol.get_root()
    while actual is not None:
        if e < actual.element:
            nodoPadre = actual
            actual = actual.left
        elif e > actual.element:
            nodoPadre = actual
            actual = actual.right
        else:
            break
    if actual is None or nodoPadre is None:
        return None
    if nodoPadre.left is actual:
        nodoHermano = nodoPadre.right
    else:
        nodoHermano = nodoPadre.left
    if nodoHermano is None:
        return None
    return nodoHermano.element


def esHoja(arbol, e):
    """True si e existe y no tiene hijos."""
    nodo = buscarNodo(arbol, e)
    if nodo is None:
        return False
    return nodo.left is None and nodo.right is None


def cantidadHijos(arbol, e):
    """Numero de hijos (0, 1 o 2) de e. -1 si e no existe."""
    nodo = buscarNodo(arbol, e)
    if nodo is None:
        return -1
    cantidad = 0
    if nodo.left is not None:
        cantidad += 1
    if nodo.right is not None:
        cantidad += 1
    return cantidad


def nivel(arbol, e):
    """Nivel (profundidad) de e: la raiz es nivel 0. -1 si no existe."""
    actual = arbol.get_root()
    nivelActual = 0
    while actual is not None:
        if e < actual.element:
            actual = actual.left
        elif e > actual.element:
            actual = actual.right
        else:
            return nivelActual
        nivelActual += 1
    return -1


def ancestros(arbol, e):
    """LinkedList con los ancestros de e, desde la raiz hasta su padre.
    Vacia si e no existe o es la raiz."""
    resultado = LinkedList()
    if buscarNodo(arbol, e) is None:
        return resultado
    actual = arbol.get_root()
    while actual.element != e:                # bajo hasta llegar a e
        resultado.addLast(actual.element)
        if e < actual.element:
            actual = actual.left
        else:
            actual = actual.right
    return resultado


def camino(arbol, e):
    """LinkedList con el camino raiz -> e (incluye e). Vacia si no existe."""
    resultado = ancestros(arbol, e)
    if buscarNodo(arbol, e) is not None:
        resultado.addLast(e)
    return resultado


def sucesor(arbol, e):
    """Menor elemento MAYOR que e (el siguiente en inorder). None si no hay."""
    candidato = None
    actual = arbol.get_root()
    while actual is not None:
        if e < actual.element:
            candidato = actual                # podria ser este; busco uno menor
            actual = actual.left
        else:
            actual = actual.right
    if candidato is None:
        return None
    return candidato.element


def predecesor(arbol, e):
    """Mayor elemento MENOR que e (el anterior en inorder). None si no hay."""
    candidato = None
    actual = arbol.get_root()
    while actual is not None:
        if e > actual.element:
            candidato = actual
            actual = actual.right
        else:
            actual = actual.left
    if candidato is None:
        return None
    return candidato.element


# ==============================================================
# 5. MEDIDAS: altura, nodos, hojas, minimo, maximo, suma
# ==============================================================

def altura(arbol):
    """Altura = aristas del camino mas largo raiz->hoja. Arbol vacio = -1.
    (Si tu profe cuenta NIVELES, cambia el caso base a 0.)"""
    return _altura(arbol.get_root())

def _altura(nodo):
    if nodo is None:
        return -1
    return 1 + max(_altura(nodo.left), _altura(nodo.right))


def contarNodos(arbol):
    return _contarNodos(arbol.get_root())

def _contarNodos(nodo):
    if nodo is None:
        return 0
    return 1 + _contarNodos(nodo.left) + _contarNodos(nodo.right)


def contarHojas(arbol):
    """Hojas = nodos sin hijos."""
    return _contarHojas(arbol.get_root())

def _contarHojas(nodo):
    if nodo is None:
        return 0
    if nodo.left is None and nodo.right is None:
        return 1
    return _contarHojas(nodo.left) + _contarHojas(nodo.right)


def contarUnHijo(arbol):
    """Nodos con exactamente un hijo."""
    return _contarUnHijo(arbol.get_root())

def _contarUnHijo(nodo):
    if nodo is None:
        return 0
    cuenta = 0
    if (nodo.left is None) != (nodo.right is None):   # solo uno es None
        cuenta = 1
    return cuenta + _contarUnHijo(nodo.left) + _contarUnHijo(nodo.right)


def arbolMenor(arbol):
    """Menor valor de un BST = el nodo mas a la IZQUIERDA."""
    actual = arbol.get_root()
    if actual is None:
        return None
    while actual.left is not None:
        actual = actual.left
    return actual.element


def arbolMayor(arbol):
    """Mayor valor de un BST = el nodo mas a la DERECHA."""
    actual = arbol.get_root()
    if actual is None:
        return None
    while actual.right is not None:
        actual = actual.right
    return actual.element


def arbolSumarTodos(arbol):
    return _sumar(arbol.get_root())

def _sumar(nodo):
    if nodo is None:
        return 0
    return nodo.element + _sumar(nodo.left) + _sumar(nodo.right)


def arbolBalanceado(arbol):
    """True si en TODOS los nodos la diferencia de alturas de sus hijos es <= 1."""
    return _balance(arbol.get_root()) != -2

def _balance(nodo):
    """Devuelve la altura, o -2 si encontro un desbalance."""
    if nodo is None:
        return -1
    izq = _balance(nodo.left)
    der = _balance(nodo.right)
    if izq == -2 or der == -2:
        return -2
    if abs(izq - der) > 1:
        return -2
    return 1 + max(izq, der)


# ==============================================================
# 6. FILTROS: menores, mayores, rangos, por nivel
# ==============================================================

def imprimirMenores(arbol, x):
    """Imprime los nodos < x (Lab 12.4 ej. 3). Si nodo >= x, todo su
    subarbol derecho tambien es >= x, asi que solo bajo por la izquierda."""
    _menores(arbol.get_root(), x)

def _menores(nodo, x):
    if nodo is None:
        return
    if nodo.element < x:
        print(nodo.element, end=" ")
        _menores(nodo.left, x)
        _menores(nodo.right, x)         # el derecho aun puede tener menores
    else:
        _menores(nodo.left, x)


def contarMayoresQue(arbol, valor):
    return _mayores(arbol.get_root(), valor)

def _mayores(nodo, valor):
    if nodo is None:
        return 0
    cuenta = 0
    if nodo.element > valor:
        cuenta = 1
    return cuenta + _mayores(nodo.left, valor) + _mayores(nodo.right, valor)


def contarMenoresQue(arbol, valor):
    return _menoresCuenta(arbol.get_root(), valor)

def _menoresCuenta(nodo, valor):
    if nodo is None:
        return 0
    cuenta = 0
    if nodo.element < valor:
        cuenta = 1
    return cuenta + _menoresCuenta(nodo.left, valor) + _menoresCuenta(nodo.right, valor)


def elementosEnRango(arbol, minimo, maximo):
    """LinkedList con los elementos en [minimo, maximo], en orden."""
    resultado = LinkedList()
    _rango(arbol.get_root(), minimo, maximo, resultado)
    return resultado

def _rango(nodo, minimo, maximo, resultado):
    if nodo is None:
        return
    if nodo.element > minimo:                 # solo si puede haber validos a la izquierda
        _rango(nodo.left, minimo, maximo, resultado)
    if minimo <= nodo.element <= maximo:
        resultado.addLast(nodo.element)
    if nodo.element < maximo:
        _rango(nodo.right, minimo, maximo, resultado)


def elementosEnNivel(arbol, nivelBuscado):
    """LinkedList con los elementos de un nivel (raiz = 0)."""
    resultado = LinkedList()
    _enNivel(arbol.get_root(), 0, nivelBuscado, resultado)
    return resultado

def _enNivel(nodo, nivelActual, nivelBuscado, resultado):
    if nodo is None:
        return
    if nivelActual == nivelBuscado:
        resultado.addLast(nodo.element)
        return
    _enNivel(nodo.left, nivelActual + 1, nivelBuscado, resultado)
    _enNivel(nodo.right, nivelActual + 1, nivelBuscado, resultado)


# ==============================================================
# 7. PROBLEMAS DE LOS LABS
# ==============================================================

def valorMasCercano(arbol, referencia):
    """Lab 12.3 ej. 2: valor del arbol mas cercano a 'referencia'.
    Bajo como en search y voy guardando el mejor candidato."""
    actual = arbol.get_root()
    mejor = None
    while actual is not None:
        if mejor is None or abs(actual.element - referencia) < abs(mejor - referencia):
            mejor = actual.element
        if referencia < actual.element:
            actual = actual.left
        elif referencia > actual.element:
            actual = actual.right
        else:
            return actual.element             # coincidencia exacta
    return mejor


def esBST(arbol):
    """Lab 12.3 ej. 3: es un BST valido?"""
    return esBSTNodo(arbol.get_root(), None, None)

def esBSTNodo(nodo, minimo, maximo):
    """Cada nodo debe estar ENTRE un limite inferior y uno superior que
    heredan de sus ancestros (no basta comparar con los hijos directos).
    Sirve tambien para arboles armados a mano con TreeNode."""
    if nodo is None:
        return True
    if minimo is not None and nodo.element <= minimo:
        return False
    if maximo is not None and nodo.element >= maximo:
        return False
    return (esBSTNodo(nodo.left, minimo, nodo.element) and
            esBSTNodo(nodo.right, nodo.element, maximo))


def ancestroComun(arbol, a, b):
    """Lab 12.4 ej. 4: ancestro comun mas cercano de a y b.
    Si ambos son menores bajo a la izquierda; si ambos mayores, a la derecha;
    el primer nodo donde se separan (o que es uno de ellos) es la respuesta."""
    if buscarNodo(arbol, a) is None or buscarNodo(arbol, b) is None:
        return None
    actual = arbol.get_root()
    while actual is not None:
        if a < actual.element and b < actual.element:
            actual = actual.left
        elif a > actual.element and b > actual.element:
            actual = actual.right
        else:
            return actual.element
    return None


def arbolesIguales(arbol1, arbol2):
    """True si los dos arboles tienen la misma forma y los mismos elementos."""
    return _igual(arbol1.get_root(), arbol2.get_root())

def _igual(nodo1, nodo2):
    if nodo1 is None and nodo2 is None:
        return True
    if nodo1 is None or nodo2 is None:
        return False
    if nodo1.element != nodo2.element:
        return False
    return _igual(nodo1.left, nodo2.left) and _igual(nodo1.right, nodo2.right)


def espejo(arbol):
    """Intercambia izquierda y derecha en todos los nodos.
    OJO: despues de esto ya NO es un BST valido."""
    _espejo(arbol.get_root())

def _espejo(nodo):
    if nodo is not None:
        nodo.left, nodo.right = nodo.right, nodo.left
        _espejo(nodo.left)
        _espejo(nodo.right)


def construirArbol(lista):
    """Crea un BinaryTree insertando los elementos de una LinkedList."""
    arbol = BinaryTree()
    actual = lista.getHead()
    while actual is not None:
        arbol.insert(actual.element)
        actual = actual.next
    return arbol


# ==============================================================
# 8. NOTAS SOBRE delete() (Lab 12.3 ej. 4) - para explicarlo en papel
# ==============================================================
# Caso 1 (current.left is None): cubre HOJA y UN SOLO HIJO DERECHO.
#     El padre se conecta con current.right (que es None si era hoja).
# Caso 2 (tiene hijo izquierdo, con o sin derecho):
#     busca el MAYOR del subarbol izquierdo (rightMost), copia su valor
#     en el nodo a eliminar y borra rightMost.
#     Si parentOfRightMost is current -> se enlaza con rightMost.left
#     Si no                           -> se enlaza con rightMost.right
#
# COMPLEJIDAD en un BST:  search/insert/delete = O(log n) si esta
# balanceado, O(n) en el peor caso (arbol "palo", elementos ya ordenados).


# ==============================================================
# PRUEBA RAPIDA: python BinaryTree_apoyo.py
# ==============================================================
if __name__ == "__main__":
    arbol = BinaryTree()
    for valor in (8, 3, 10, 1, 6, 14, 4, 7, 13):
        arbol.insert(valor)
    print("Inorder  :", inorderLista(arbol))
    print("Preorder :", preorderLista(arbol))
    print("Postorder:", postorderLista(arbol))
    print("Niveles  :", porNivelesLista(arbol))
    print("Altura:", altura(arbol), "| Hojas:", contarHojas(arbol))
    print("Menores que 7:", end=" ")
    imprimirMenores(arbol, 7)
    print()
    print("Ancestro comun de 4 y 7:", ancestroComun(arbol, 4, 7))
    print("Es BST:", esBST(arbol))
