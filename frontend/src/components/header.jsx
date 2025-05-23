import Navbar from "./navbar";

export default function Header(){
    return(
        <>
            <header className=" w-full h-14 relative">
                <div className="flex flex-grow fixed h-14 w-full">
                    <div className=" h-full border flex items-center backdrop-blur-3xl">
                        <img src="logo.gif" alt="Logo" className=" h-full w-20"/>
                    </div>
                    <Navbar/>
                </div>
            </header>
        </>
    )
}