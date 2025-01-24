# CV Backend - Proyecto Django - Docs

Explicación de los modelos y su funcionamiento en el administrador de Django.

---

## Tabla de Contenidos

1. [descripción general](#descripción-general)
2. [BaseModel](#modelo-de-basemodel)
3. [Tags](#modelo-tag)

---

## Descripción General

El modelo `Core` es la aplicación principal del proyecto se encarga de gestionar modelos comunes como los `Sigelton` y los `Metadatos` de las otras apps.

# Modelo de `BaseModel`

- **Nombre del Modelo**: `BaseModel`
- **Tipo**: Modelo abstracto
- **Propósito**: Proveer campos comunes para el seguimiento de creación y modificación de registros.

---

### Campos

| Campo                    | Tipo            | Descripción                                                                                                                 |
| ------------------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **`creado_por`**         | `ForeignKey`    | Referencia al usuario que creó el registro. Si el usuario es eliminado, el valor se establece en `NULL`.                    |
| **`modificado_por`**     | `ForeignKey`    | Referencia al usuario que modificó el registro por última vez. Si el usuario es eliminado, el valor se establece en `NULL`. |
| **`fecha_creacion`**     | `DateTimeField` | Fecha y hora en que el registro fue creado. No editable. Se establece automáticamente al momento de la creación.            |
| **`fecha_modificacion`** | `DateTimeField` | Fecha y hora de la última modificación. Se actualiza automáticamente cada vez que se guarda el registro.                    |

### Meta

- **`abstract`**: Este modelo no se migrará como tabla a la base de datos, ya que está diseñado para ser heredado por otros modelos.

### Características Adicionales

- **Seguimiento de usuarios**: Vincula las acciones de creación y modificación de registros con usuarios específicos.
- **Auditoría de registros**: Facilita el seguimiento del historial de cambios al registrar fechas de creación y modificación.
- **Herencia**: Puede ser extendido por otros modelos para centralizar la lógica de auditoría en un único lugar.

---

# Modelo `Tag`

El modelo `Tag` se utiliza para gestionar etiquetas que pueden ser asociadas a otros modelos del proyecto. Cada etiqueta incluye un nombre único y un color personalizado.

## Descripción de `Tag`

- **Nombre del Modelo**: `Tag`
- **Propósito**: Proveer etiquetas con nombre y color para clasificar o categorizar elementos en el proyecto.

## Campos

| Campo        | Tipo         | Descripción                                          |
| ------------ | ------------ | ---------------------------------------------------- |
| **`nombre`** | `CharField`  | Nombre único del tag. Máximo de 100 caracteres.      |
| **`color`**  | `ColorField` | Color asociado al tag. Valor por defecto: `#FF0000`. |

## Meta

- **`verbose_name`**: "Tag"
- **`verbose_name_plural`**: "Tags"

## Características Adicionales

- **Nombre único**: Garantiza que no existan etiquetas duplicadas al requerir unicidad en el campo `nombre`.
- **Colores personalizables**: Permite asociar un color único a cada etiqueta para visualizaciones o identificaciones rápidas.

---
