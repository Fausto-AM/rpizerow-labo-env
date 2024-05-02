#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/kthread.h>
#include <linux/sched.h>
#include <linux/delay.h>
#include <linux/sched/signal.h>

// Variables globales para kernel threads
static struct task_struct *kthread_1 = NULL;
static struct task_struct *kthread_2 = NULL;

// TODO:
// Funciones para los hilos}
// Crea una función para el Hilo llamada hilo_01.
static int hilo_01(void *params) {
// Mientras el Hilo no sea interrumpido, el programa printeará el string con un delay
	while(!kthread_should_stop()) {
		printk("AlvarezMollo_Fausto_ej02: Hola desde el primer hilo");
		msleep(100);
	}
	return 0;
}
// Crea una función para el Hilo llamada hilo_02.
static int hilo_02(void *params) {
	while(!kthread_should_stop()) {
		printk("AlvarezMollo_Fausto_ej02: Hola desde el segundo hilo");
		msleep(100);
	}
	return 0;
}
/**
 * @brief Se llama cuando se carga en el kernel
*/
static int __init ej02_module_init(void) {
	// TODO:
	// - Crear ambos hilos
	// - Verificar que se hayan podido crear
	// - Correr hilos

// Crea el Hilo 1 con la función hilo_01
	kthread_1 = kthread_create(hilo_01, NULL, "Hilo 1");
// En caso de que el Hilo devuelva NULL (No se haya creado), printeará un mensaje de error.
	if (kthread_1 ==  NULL) {
		printk("AlvarezMollo_Fausto_ej02: No se pudo crear el Hilo 1.");
		return -1;
	}
// Crea el Hilo 2 con la función hilo_02
	kthread_2 = kthread_create(hilo_02, NULL, "Hilo 2");
	if (kthread_2 ==  NULL) {
		printk("AlvarezMollo_Fausto_ej02: No se pudo crear el Hilo 2.");
		return -1;
	}
// Despierta los Hilos 1 y 2.
	wake_up_process(kthread_1);
	wake_up_process(kthread_2);
	return 0;
}

/**
 * @brief Se llama cuando se retira del kernel
*/
static void __exit ej02_module_exit(void) {
	// TODO:
	// - Detener hilos
// Detiene los Hilos.
	kthread_stop(kthread_1);
	kthread_stop(kthread_2);
}

// Registro funciones de inicializacion y salida
module_init(ej02_module_init);
module_exit(ej02_module_exit);

// Informacion del modulo (completar lo que corresponda)
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Fausto Alvarez Mollo");
MODULE_DESCRIPTION("");
