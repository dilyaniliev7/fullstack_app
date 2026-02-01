import {React, useState, useEffect} from 'react'
import AxiosInstance from "./Axios"
import {Box, Typography} from "@mui/material"
import AddBoxIcon from '@mui/icons-material/AddBox';

const Create = () => {
    const [country, setCountry] = useState([])
    const [league, setLeague] = useState([])
    const [characteristic, setCharacteristic] = useState([])
    const GetData = () => {
        AxiosInstance.get(`country/`).then((res) => {
            setCountry(res.data)
            })
        AxiosInstance.get(`league/`).then((res) => {
            setLeague(res.data)
            })
        AxiosInstance.get(`characteristic/`).then((res) => {
            setCharacteristic(res.data)
            })
        }
    useEffect(() => {
        GetData()
        }, [])
    return (
        <div>
            <Box className="TopBar">
                <AddBoxIcon/>
                <Typography sx={{marginLeft: '15px', fontWeight: 'bold'}} variant='subtle2'>Create a new club!</Typography>
            </Box>

            <Box className={"FormBox"}>
                <Box className={"FormArea"}>

                </Box>

                <Box className={"FormArea"}>

                </Box>

                <Box className={"FormArea"}>

                </Box>
            </Box>
        </div>
        )
    }

export default Create