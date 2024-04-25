#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>

/**
 * @brief Se llama cuando se carga en el kernel
*/
static int __init ej01_module_init(void) {
	// Completar
	printk("alvarezmollo_fausto_ej01: Hola desde Kernel!");
	// Salio todo bien
	return 0;
}

/**
 * @brief Se llama cuando se retira del kernel
*/
static void __exit ej01_module_exit(void) {
	// Completar
	printk("alvarezmollo_fausto_ej01: Chau desde Kernel!");
}

// Registro funciones de inicializacion y salida
module_init(ej01_module_init);
module_exit(ej01_module_exit);

// Informacion del modulo (completar lo que corresponda)
MODULE_LICENSE("GPL");
MODULE_AUTHOR("ALVAREZ MOLLO, FAUSTO");
MODULE_DESCRIPTION("Cada vez que entrás al kernel manda un mensaje de bienvenida. Cada vez que salís manda un mensaje de despedida.");
