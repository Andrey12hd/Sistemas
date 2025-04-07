import { Text, View, StyleSheet } from "react-native";
import { Image } from "expo-image"
import { Ionicons } from "@expo/vector-icons"

// npm install expo-image (usar este código no terminal)

const foto = require("../assets/images/gamba.jpeg")

export default function Index() {
  return (
    <View style={styles.container} >
      <View style = {styles.containerImg}>
        <Image source = {foto} style={styles.estiloFoto}></Image>
      </View>
      <View style = {styles.containerConteudo}>
        <View style = {styles.containerNome}>
          <Text style={styles.nome}>Senhor Corin</Text>
        </View>
        <Text style = {styles.linha}>
          _____________________________
        </Text>
        <View style = {styles.containerDados}>
          <Ionicons name="person" size={24} color="black" />
          <Text style = {styles.textoDados}>18 anos</Text>
        </View>
        <View style = {styles.containerDados}>
          <Ionicons name="mail" size={24} color="red" />
          <Text style = {styles.textoDados}>corindachuva@escola.pr.gov.br</Text>
        </View>
        <View style = {styles.containerDados}>
          <Ionicons name="call" size={24} color="green" />
          <Text style = {styles.textoDados}>(41) 98404-2436</Text>
        </View>
        <View style = {styles.containerDados}>
          <Ionicons name="home" size={24} color="yellow" />
          <Text style = {styles.textoDados}>Ponta Grossa / PR  Brasil</Text>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "grey"
  },
  containerImg: {
    flex: 1,
    paddingTop: 60,
  },
  estiloFoto: {
    width: 300,
    height: 300,
  },
  containerConteudo: {
    flex: 1
  },
  containerNome:{
    alignItems:"center",
  },
  nome: {
    fontSize: 40,
    color: "black",
    fontWeight: "bold",
  },
  linha:{
    color: "white",
    fontSize: 20,
    marginBottom: 20
  },
  containerDados: {
    marginBottom: 8,
    flexDirection: "row",
    alignItems: "center",
  },
  textoDados: {
    marginLeft: 10,
    color: "cyan",
    fontSize: 24,
  }
})