# 🇳🇬 Nigeria GeoJSON API

A comprehensive, structured, and ready-to-use dataset of all **States**, **Local Government Areas (LGAs)**, and **Wards** in Nigeria, including their **geographic coordinates**.

Ideal for developers, civic tech, GIS, mapping tools, and data-driven apps.

---

## 📁 Folder: `data/`

| File | Description |
|------|-------------|
| `states.json` | List of all Nigerian states (36 + FCT) |
| `lgas.json` | Object mapping each state to its list of LGAs |
| `wards.json` | Flat list of all wards with their lat/long |
| `lgas-with-wards.json` | Nested object: state → LGA → wards |
| `full.json` | 🔥 All-in-one structure: state → LGA → wards with coordinates |

---

## 🔎 File Structure Examples

### `states.json`
```json
["Abia", "Adamawa", "Akwa Ibom", ..., "Zamfara"]
```

### `lgas.json`
```json
{
  "Kwara": ["Ilorin East", "Ilorin South", "Ilorin West", ...],
  ...
}
```

### `wards.json`
```json
[
  {
    "State": "Kwara",
    "LGA": "Ilorin West",
    "Ward": "Ajikobi",
    "Latitude": 8.4892,
    "Longitude": 4.5382
  },
  ...
]
```

### `lgas-with-wards.json`
```json
{
  "Kwara": {
    "Ilorin West": [
      {
        "name": "Ajikobi",
        "latitude": 8.4892,
        "longitude": 4.5382
      },
      ...
    ]
  }
}
```

### `full.json`
```json
[
  {
    "state": "Kwara",
    "lgas": [
      {
        "name": "Ilorin West",
        "wards": [
          {
            "name": "Ajikobi",
            "latitude": 8.4892,
            "longitude": 4.5382
          },
          ...
        ]
      }
    ]
  }
]
```

---

## 🚀 How to Use

Host the files on:
- GitHub Pages
- Netlify / Vercel
- Local or cloud-based APIs

Then fetch like:
```js
fetch("/data/full.json").then(res => res.json());
```

---

## 📌 Use Cases

- ✅ Election & civic apps
- ✅ State/LGA/Ward dropdowns
- ✅ Offline mapping and analytics
- ✅ Data validation for forms
- ✅ Location-based services in Nigeria

---

## 📜 License

**MIT** – free to use, modify, and distribute.  
Attribution is appreciated but not required.

---

## 🙌 Contributions

Found an error or want to add metadata (region, postal codes, coordinates)?  
PRs welcome!
